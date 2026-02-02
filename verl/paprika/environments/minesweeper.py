import re
from typing import List, Dict, Union, Optional, Any, Tuple
from copy import deepcopy
import random
from collections import deque
import json

from verl.paprika.environments.base_env import BaseEnv
from verl.paprika.environments.env_configs.minesweeper_config import (
    MINESWEEPER_ENV_DATA,
)

# Different rewards for minesweeper
MINESWEEPER_DEFAULT_REWARD_FOR_UNSOLVED_TASK = 0.0
MINESWEEPER_DEFAULT_REWARD_FOR_SOLVED_TASK = 20.0
MINESWEEPER_PER_TURN_FORMAT_PENALTY = -1.0
MINESWEEPER_HIT_MINE_PENALTY = -1.0
MINESWEEPER_PER_TURN_PENALTY = -1.0


class MinesweeperEnv(BaseEnv):
    """
    Inspired by: https://en.wikipedia.org/wiki/Minesweeper_(video_game)
    made into a text-based Minesweeper environment. It interprets user moves like:
    "reveal 2 3"
    which updates the board and returns feedback.
    If there is a mine in the position, the game will be over.
    If there are mines in adjacent cells, the number will be revealed.
    If there are 0 mines in adjacent cells, there will be a BFS flood fill reveal.
    """

    custom_system_prompt_str = (
        "You are a helpful assistant."
    )

    default_system_prompt_str = "You are a helpful assistant."

    def __init__(
        self,
        task_state: Dict[str, Any],
        mode: str = "train",
    ):
        task_state = deepcopy(task_state)
        # Retrieve minesweeper board configuration
        assert "env" in task_state
        assert "agent" in task_state

        task_state["env"] = json.loads(deepcopy(task_state["env"]))
        task_state["agent"] = json.loads(deepcopy(task_state["agent"]))

        assert (
            isinstance(task_state["env"], dict)
            and isinstance(task_state["env"].get("rows"), int)
            and isinstance(task_state["env"].get("cols"), int)
            and isinstance(task_state["agent"], dict)
        )
        self.rows = task_state["env"]["rows"]
        self.cols = task_state["env"]["cols"]
        self.initial_board_view = deepcopy(task_state["agent"]["initial_board_view"])

        self.revealed = set()
        self.adjacent_counts = {}

        self.mode = mode
        assert self.mode in ["train", "test"]

        # If mode is train, then retrive board
        # First agent move is pre-defined, to keep the same board for all instance
        # of the same environment
        if self.mode == "train":
            assert isinstance(task_state["env"].get("mine_positions"), list)
            assert len(task_state["env"]["mine_positions"]) > 0
            list_of_mine_positions = deepcopy(task_state["env"]["mine_positions"])

            mine_positions = []
            for mine_position in list_of_mine_positions:
                assert isinstance(mine_position, list)
                assert len(mine_position) == 2
                mine_positions.append(tuple(mine_position))

            self.mine_positions = set(mine_positions)
            self.num_safe_cells = (self.rows * self.cols) - len(self.mine_positions)

            assert isinstance(task_state["agent"].get("first_agent_move"), list)
            assert len(task_state["agent"]["first_agent_move"]) == 2

            self.mandatory_first_agent_move = tuple(task_state["agent"]["first_agent_move"])
            self.first_move_constraint_satisfied = False

        else:
            self.mine_positions = set()

            assert isinstance(task_state["env"].get("random_mine_count"), int)
            self.random_mine_count = task_state["env"]["random_mine_count"]

        self.trajectory_level_reward = MINESWEEPER_DEFAULT_REWARD_FOR_UNSOLVED_TASK

    def get_start_state(self) -> str:
        if self.mode == "train":
            return MINESWEEPER_ENV_DATA["start_state_for_training"].format(
                initial_board_view=self.initial_board_view,
                mandatory_first_agent_move_row=self.mandatory_first_agent_move[0],
                mandatory_first_agent_move_col=self.mandatory_first_agent_move[1],
            )
        else:
            return MINESWEEPER_ENV_DATA["start_state_for_test"].format(
                initial_board_view=self.initial_board_view,
            )
    
    def get_max_num_tokens_per_turn(self) -> Optional[int]:
        return 1024
    
    def extract_response(
        self,
        response: str,
    ) -> str:
        """
        Given a response string, potentially with a chain-of-thought
        and a final answer, this function returns the final answer,
        to generate the rule based next state.

        Args:
            response (str):
                LLM generated response. 

                Example: 
                    <Think> Step-by-step thinking </Think> <Answer> TOTEM </Answer>

        Returns:
            str: 
                The extracted answer between <Answer> and </Answer> tokens

                Example:
                    In the above example, we would return "TOTEM"
        """
        match = re.search(r"<Answer>(.*?)</Answer>", response, re.DOTALL)

        if match:
            return match.group(1).strip().lower()
        
        else:
            raise ValueError(f"Given response {response} is invalid")
        
    def get_max_turns(self) -> int:
        return MINESWEEPER_ENV_DATA["max_turns"]
    
    def get_custom_system_prompt(
       self     
    ) -> str:
        return self.custom_system_prompt_str
    
    def get_default_system_prompt(self) -> str:
        return self.default_system_prompt_str
    
    def get_system_prompt(self) -> str:
        return self.default_system_prompt_str
    
    def _parse_reveal_command(
        self,
        msg: str,
    ) -> Tuple[Optional[int], Optional[int]]:
        """
        Only accepts "reveal <row> <col>".
        Returns (row, col) or raises Error if parsing fails.
        """
        pattern = r"^reveal\s+(\d+)\s+(\d+)$"
        match = re.search(pattern, msg)

        if match:
            return int(match.group(1)), int(match.group(2))
        
        else:
            raise ValueError(f"Given reveal command could not be parsed.")
        
    def place_mines_excluding_first_agent_move(
        self,
        safe_r: int,
        safe_c: int,
        total_mines: int,
    ) -> None:
        all_cells = [
            (r, c)
            for r in range(self.rows)
            for c in range(self.cols)
        ]

        all_cells.remove((safe_r, safe_c))
        mine_cells = random.sample(
            all_cells,
            min(total_mines, len(all_cells))
        )

        self.mine_positions = set()
        for cell in mine_cells:
            self.mine_positions.add(cell)

        self.num_safe_cells = (self.rows * self.cols) - len(self.mine_positions)

    def count_adj_mines(
        self,
        row: int,
        col: int,
    ) -> int:
        count = 0
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if (r, c) in self.mine_positions:
                    count += 1

        return count
    
    def flood_fill(
        self,
        start_r: int,
        start_c: int,
    ) -> None:
        """
        flood fill for any revealed cell that has 0 adjacent mines.
        Expands to neighbors that are not mines and not revealed yet.
        """
        queue = deque()
        queue.append((start_r, start_c))

        while queue:
            r, c = queue.popleft()

            for rr in range(r - 1, r + 2):
                for cc in range(c - 1, c + 2):
                    if 0 <= rr < self.rows and 0 <= cc < self.cols:
                        if (rr, cc) not in self.mine_positions and (
                            rr,
                            cc,
                        ) not in self.revealed:
                            self.revealed.add((rr, cc))
                            adj_count = self.count_adj_mines(rr, cc)
                            self.adjacent_counts[(rr, cc)] = adj_count
                            if adj_count == 0:
                                queue.append((rr, cc))

    def check_victory(self) -> bool:
        """
        Check if all safe cells have been revealed.
        """
        return len(self.revealed) == self.num_safe_cells
    
    def _render_board_message(self) -> str:
        """
        Returns a text-based partial board for debugging/feedback.
        If adjacency == 0, display '*'.
        Else display the adjacency count.
        Hidden cells remain '#' until the game is over (win or lose).
        Once game_over is True, display all mines as 'M'.
        """
        lines = []

        for r in range(self.rows):
            row_chars = []
            for c in range(self.cols):
                if (r, c) in self.revealed and (r, c) not in self.mine_positions:
                    count = self.adjacent_counts.get((r, c), 0)
                    row_chars.append(str(count) if count > 0 else "*")
                else:
                    row_chars.append("#")
            lines.append(" ".join(row_chars))

        return "\n".join(lines)
    
    def render_full_board_with_all_mines(self) -> str:
        lines = []

        for r in range(self.rows):
            row_chars = []
            for c in range(self.cols):
                if (r, c) in self.mine_positions:
                    row_chars.append('M')

                else:
                    row_chars.append('.')

            lines.append(" ".join(row_chars))

        return "\n".join(lines)

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

        # Check if <Answer> </Answer> tags are used correctly
        try:
            agent_action = self.extract_response(response=last_assistant_response)
        except:
            self.trajectory_level_reward += MINESWEEPER_PER_TURN_FORMAT_PENALTY
            return {
                "content": MINESWEEPER_ENV_DATA["environment_default_response"],
                "goal_reached": False,
                "judge_label": False,
            }
        
        # Check if row and column are in correct format  
        # within the <Answer> </Answer> tags
        try:
            row, col = self._parse_reveal_command(
                msg=agent_action,
            )
        
        except:
            feedback = (
                "Invalid move format. Use: 'reveal <row> <col>'. Example: 'reveal 1 3'."
            )
            feedback += MINESWEEPER_ENV_DATA["agent_optional_message"]

            self.trajectory_level_reward += MINESWEEPER_PER_TURN_FORMAT_PENALTY

            return {
                "content": feedback,
                "goal_reached": False,
                "judge_label": False,
            }
        
        # In case we are doing training, check if the first move by the agent
        # Is indeed the first move given in the task instruction
        if self.mode == "train":
            if not self.first_move_constraint_satisfied and not (
                row == self.mandatory_first_agent_move[0]
                and col == self.mandatory_first_agent_move[1]
            ):
                feedback = (
                    "You did not choose the first move according to "
                    "the instruction you were given. "
                    "The first move has to be "
                    f"reveal {self.mandatory_first_agent_move[0]} {self.mandatory_first_agent_move[1]}."
                )

                self.trajectory_level_reward += MINESWEEPER_PER_TURN_FORMAT_PENALTY

                return {
                    "content": feedback,
                    "goal_reached": False,
                    "judge_label": False,
                }
            
            else:
                self.first_move_constraint_satisfied = True

        # Check if (row, column) that the agent asked to be revealed
        # is valid or not
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            feedback = (
                f"Invalid move: ({row},{col}) is out of bounds "
                f"(valid range: rows between 0 and {self.rows-1}, "
                f"cols betweewn 0 and {self.cols-1})"
            )

            self.trajectory_level_reward += MINESWEEPER_PER_TURN_PENALTY

            return {
                "content": feedback,
                "goal_reached": False,
                "judge_label": False,
            }
        
        # Check if the agent chose a (row, col) position that 
        # it has chosen before
        if (row, col) in self.revealed:
            feedback = f"Cell ({row},{col}) is already revealed."

            self.trajectory_level_reward += MINESWEEPER_PER_TURN_PENALTY

            return {
                "content": feedback,
                "goal_reached": False,
                "judge_label": False,
            }
        
        # If in test mode, generate the rest of the board here
        if self.mode == "test":
            if len(self.mine_positions) == 0 and len(self.revealed) == 0:
                self.place_mines_excluding_first_agent_move(
                    safe_r=row,
                    safe_c=col,
                    total_mines=self.random_mine_count,
                )

        self.revealed.add((row, col))

        # Hit a mine, so game over
        if (row, col) in self.mine_positions:
            feedback = (
                f"BOOM! You hit a mine at ({row},{col}). "
                "The board with all mine positions looks like: "
            )
            feedback += self.render_full_board_with_all_mines()
            feedback += "<End> Game over </End>"

            self.trajectory_level_reward += MINESWEEPER_HIT_MINE_PENALTY

            return {
                "content": feedback,
                "goal_reached": True,
                "judge_label": False,   # Game over but unsuccessful trajectory
            }
        
        adj_mines = self.count_adj_mines(row, col)
        self.adjacent_counts[(row, col)] = adj_mines

        if adj_mines == 0:
            self.flood_fill(row, col)

        # Game won
        if self.check_victory():
            self.trajectory_level_reward += MINESWEEPER_DEFAULT_REWARD_FOR_SOLVED_TASK

            return {
                "content": "Goal reached",
                "goal_reached": True,
                "judge_label": True,
            }
        
        # Intermediate step
        feedback = self._render_board_message()
        feedback += MINESWEEPER_ENV_DATA["agent_optional_message"]
        self.trajectory_level_reward += MINESWEEPER_PER_TURN_PENALTY

        return {
            "content": feedback,
            "goal_reached": False,
            "judge_label": False,
        }
        