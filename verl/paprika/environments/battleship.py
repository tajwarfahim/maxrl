import re
from typing import List, Dict, Union, Optional, Tuple, Any
from copy import deepcopy
import json

from verl.paprika.environments.base_env import BaseEnv
from verl.paprika.environments.env_configs.battleship_config import (
    BATTLESHIP_ENV_DATA,
)

# Different rewards for battleship
BATTLESHIP_DEFAULT_REWARD_FOR_UNSOLVED_TASK = 0.0
BATTLESHIP_DEFAULT_REWARD_FOR_SOLVED_TASK = 20.0
BATTLESHIP_PER_TURN_FORMAT_PENALTY = -1.0
BATTLESHIP_PER_TURN_CORRECTLY_FORMATTED_BUT_SUBOPTIMAL_ACTION_PENALTY = 0.0
BATTLESHIP_PER_TURN_REWARD = 0.0


class BattleshipEnv(BaseEnv):
    """
    Inspired by: https://en.wikipedia.org/wiki/Battleship_(game)
    Slightly modfied due to making it a single-player Battleship engine. 
    """

    custom_system_prompt_str = (
        "You are a helpful assistant."
    )

    default_system_prompt_str = "You are a helpful assistant."

    ship_sizes = {
        "Carrier": 5,
        "Battleship": 4,
        "Destroyer": 2
    }

    def __init__(
        self,
        task_state: Dict[str, Any],
        mode: str = "train",
    ):
        task_state = deepcopy(task_state)
        assert "env" in task_state
        assert "agent" in task_state

        task_state["env"] = json.loads(deepcopy(task_state["env"]))

        # Recover game states
        self.initial_board_string_representation = deepcopy(task_state["agent"])
        self.board = deepcopy(task_state["env"]["hidden_board_representation"])
        
        assert isinstance(self.board, list)
        for row in self.board:
            assert isinstance(row, list)

            # Check square grid
            assert len(row) == len(self.board)

            for cell in row:
                assert isinstance(cell, str)

        self.grid_size = len(self.board)
        self.ship_cells_hit = 0
        self.total_ship_cells = sum(self.ship_sizes.values())

        # Reconstruct ship positions in Dict[str, Set[Tuple[int, int]]]
        # To be reusable with code from Paprika
        ship_positions = deepcopy(task_state["env"]["ship_positions"])
        ship_position_reconstituted = {
            ship_name: set() 
            for ship_name in self.ship_sizes
        }
        for ship_name in ship_position_reconstituted:
            ship_positions_list = ship_positions[ship_name]
            for cell_location in ship_positions_list:
                ship_position_reconstituted[ship_name].add(
                    tuple(cell_location)
                )

        self.ship_positions = ship_position_reconstituted
        self.guesses_made = 0

        # Other env variables
        self.mode = mode
        self.trajectory_level_reward = BATTLESHIP_DEFAULT_REWARD_FOR_UNSOLVED_TASK
        assert self.mode in ["train", "test"]

    def get_start_state(self) -> str:
        return BATTLESHIP_ENV_DATA["agent"].format(
            agent=self.initial_board_string_representation,
            max_attempts=BATTLESHIP_ENV_DATA["max_turns"],
        )
    
    def get_max_num_tokens_per_turn(self) -> Optional[int]:
        return 1024
    
    def extract_response(
        self,
        response: str,
    ) -> Tuple[str, int, str]:
        """
        Given a response string, potentially with a chain-of-thought
        and a final answer, this function returns the final answer,
        to generate the rule based next state.

        Args:
            response (str):
                LLM generated response. 

                Example: 
                    <Think> Step-by-step thinking </Think> <Answer> A1 </Answer>

        Returns:
            str: 
                The extracted answer between <Answer> and </Answer> tokens
        """
        match = re.search(r"<Answer>(.*?)</Answer>", response, re.DOTALL)

        if match:
            guess_text = match.group(1).strip().upper()

            pattern = r"^([A-Z])(\d{1,2})$"
            match = re.match(pattern, guess_text)

            if not match:
                raise ValueError(f"Given response {response} is invalid")
            
            row_letter = match.group(1)
            col_number = int(match.group(2))
            agent_action = row_letter + str(col_number)

            return row_letter, col_number, agent_action
        
        else:
            raise ValueError(f"Given response {response} is invalid")
        
    def get_max_turns(self) -> int:
        return BATTLESHIP_ENV_DATA["max_turns"]
    
    def get_custom_system_prompt(
       self     
    ) -> str:
        return self.custom_system_prompt_str
    
    def get_default_system_prompt(self) -> str:
        return self.default_system_prompt_str
    
    def get_system_prompt(self) -> str:
        return self.default_system_prompt_str
    
    def _board_to_string(self) -> str:
        """
        This is the board represenation that the agent will obtain.
        This means ship locations not revealed yet, remains hidden.
        """
        header_nums = " ".join(str(i + 1).rjust(2) for i in range(self.grid_size))
        header = f"    {header_nums}"

        rows = []

        for r in range(self.grid_size):
            row_label = chr(ord('A') + r)
            row_cells = []

            for c in range(self.grid_size):
                val = self.board[r][c]

                if val == "S":
                    row_cells.append(".")

                else:
                    row_cells.append(val)

            row_str = " ".join(cell.rjust(2) for cell in row_cells)
            rows.append(f"{row_label}  {row_str}")

        return header + "\n" + "\n".join(rows)

    def step(
        self,
        conversation_history: List[Dict[str, str]],
    ) -> Dict[str, Union[str, bool]]:
        self.validate_conversation_history(
            conversation_history=conversation_history,
        )

        # Preliminary checks on the conversation_history
        assert len(conversation_history) >= 2

        assert conversation_history[-1]["role"] == "assistant"
        last_assistant_response = conversation_history[-1]["content"]

        try:
            row_letter, col_number, agent_action = self.extract_response(
                response=last_assistant_response,
            )

        # Ill-formed response
        except:
            feedback: str = (
                f"Invalid guess. "
                f"Please guess A1, B3, etc. "
                f"where A1 means first cell of first row, "
                f"B3 means third cell of second row and so on. "
            )

            feedback += BATTLESHIP_ENV_DATA["agent_optional_message"]

            self.trajectory_level_reward += BATTLESHIP_PER_TURN_FORMAT_PENALTY

            return {
                "content": feedback,
                "goal_reached": False,
                "judge_label": False,
            }
        
        # Out-of-range row
        row_index = ord(row_letter) - ord("A")
        if not (0 <= row_index < self.grid_size):
            max_row_letter = chr(ord("A") + self.grid_size - 1)
            feedback = (
                f"Row '{row_letter}' is out of range. Valid rows are A..{max_row_letter}."
            )

            self.trajectory_level_reward += BATTLESHIP_PER_TURN_CORRECTLY_FORMATTED_BUT_SUBOPTIMAL_ACTION_PENALTY

            return {
                "content": feedback,
                "goal_reached": False,
                "judge_label": False,
            }
        
        # Out-of-range column
        if not (1 <= col_number <= self.grid_size):
            feedback = f"Column {col_number} out of range. Must be 1..{self.grid_size}."

            self.trajectory_level_reward += BATTLESHIP_PER_TURN_CORRECTLY_FORMATTED_BUT_SUBOPTIMAL_ACTION_PENALTY
            
            return {
                "content": feedback,
                "goal_reached": False,
                "judge_label": False,
            }
        
        # Valid action generated by the LLM
        # So execute the action and return the environment stage after that
        game_won = False
        col_index = col_number - 1

        self.guesses_made += 1
        cell_value = self.board[row_index][col_index]

        if cell_value == "S":
            self.board[row_index][col_index] = "X"
            self.ship_cells_hit += 1

            just_sank_ship = False
            sunk_ship_name = None
            hit_ship_name = None

            for ship_name, positions in self.ship_positions.items():
                if (row_index, col_index) in positions:
                    positions.remove((row_index, col_index))
                    hit_ship_name = ship_name

                    if len(positions) == 0:
                        just_sank_ship = True
                        sunk_ship_name = ship_name

                    break

            # Game won
            if self.ship_cells_hit == self.total_ship_cells:
                feedback = (
                    f"Hit at {agent_action}! You sank the {sunk_ship_name}!\n"
                    f"You have sunk all ships in {self.guesses_made} guesses. "
                    f"You Won! Goal reached."
                )

                game_won = True
                self.trajectory_level_reward += BATTLESHIP_DEFAULT_REWARD_FOR_SOLVED_TASK
            
            # Game not won, but partial hit
            else:
                feedback = f"Hit at {agent_action}!"
                self.trajectory_level_reward += BATTLESHIP_PER_TURN_REWARD

                if just_sank_ship:
                    feedback += f" You sank the {sunk_ship_name}!"

                else:
                    feedback += (
                        f" You have hit a {hit_ship_name}, which occupies "
                        f"{self.ship_sizes[hit_ship_name]} cells in the grid.\n"
                    )

                feedback += " Here is how the board looks now: \n" + self._board_to_string()

        elif cell_value in ("X", "M"):
            feedback = (
                f"You already guessed {agent_action}. Please make another guess!"
            )

            self.trajectory_level_reward += BATTLESHIP_PER_TURN_CORRECTLY_FORMATTED_BUT_SUBOPTIMAL_ACTION_PENALTY

            feedback += " Here is how the board looks now: \n" + self._board_to_string()

        else:
            self.board[row_index][col_index] = "M"

            feedback = (
                f"Miss at {agent_action}. There is no ship in this co-ordinate."
            )

            feedback += " Here is how the board looks now: \n" + self._board_to_string()
        
        return {
            "content": feedback,
            "goal_reached": game_won,
            "judge_label": game_won,
        }
