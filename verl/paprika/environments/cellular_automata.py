from typing import List, Dict, Union, Optional, Any
from copy import deepcopy

from verl.paprika.environments.base_env import BaseEnv
from verl.paprika.environments.env_configs.cellular_automata_config import (
    CELLULAR_AUTOMATA_ENV_DATA,
)

CELLULAR_AUTOMATA_DEFAULT_REWARD_FOR_UNSOLVED_TASK = 0.0
CELLULAR_AUTOMATA_DEFAULT_REWARD_FOR_SOLVED_TASK = 1.0


def generate_next_state_1D_cellular_automatation(
    current_state: List[str],
    automation_rule: Dict[str, str],
) -> List[int]:
    """
    Generates the next state from the current state
    in a 1D elementary cellular automation,
    as described here: https://en.wikipedia.org/wiki/Elementary_cellular_automaton

    Input:
        current_state (List[str]):
            The current state of the automation
            Typically would be a list, with each element being '0' or '1'
            (though we don't enforce it, as long as the ruleset supports it)

            Example:
                ['0', '1', '1', '1', '1', '0']

        automation_rule (Dict[str, str]):
            The rules that define the transition
            We consider only a particular cell, its left and right neighbors
            (possibly in a warped style), and use the rule given by automation_rule
            to update it.

            Example:
                {
                    '111': '0',
                    '110': '1',
                    '101': '1',
                    '100': '0',
                    '011': '1',
                    '010': '1',
                    '001': '1',
                    '000': '0',
                }

    Output:
        next_state (List[str]):
            The next state of the automation,
            obtained from the inputs

            We consider a particular cell and its immediate neighbors (potentially
            in a warp-around edge way), to calculate the next state.

            Example:
                Assume the example inputs above. Using the automation rule,
                consider each cell's left neighbor, the cell itself, and the right neighbor

                We look it up in our rule dictionary, which dictates what the cell in the
                same position, but in the next state should be.

                '001' -> '1', so the first cell becomes '1'
                '011' -> '1', so the second cell becomes '1'
                '111' -> '0', so the third cell becomes '0'
                '111' -> '0', so the fourth cell becomes '0'
                '110' -> '1', so the fifth cell becomes '1'
                '100' -> '0', so the sixth cell becomes '0'

                Therefore, the next state shall be: ['1', '1', '0', '0', '1', '0']
    """
    next_state = []

    for i in range(len(current_state)):
        left = current_state[(i - 1) % len(current_state)]
        right = current_state[(i + 1) % len(current_state)]
        curr = current_state[i]

        neighborhood = f"{left}{curr}{right}"
        if neighborhood not in automation_rule:
            raise ValueError(
                f"Given automation_rule does not contain neighborhood {neighborhood}"
            )

        next_state.append(automation_rule[neighborhood])

    return next_state


def extract_inputs(text: str) -> List[str]:
    """
    Given a string of a particular format, extracts
    all the inputs, and returns them.

    Input:
        text (str):
            Usually has the following format:
            "
            Input 1: ....
            Output 1: ....

            Input 2: ....
            Output 2: ....
            "

    Output:
        all_input_list (List[str]):
            List of all the inputs in the text string
    """
    input_num = 1
    all_input_list = []

    while True:
        if f"Input {input_num}:" not in text or f"Output {input_num}:" not in text:
            break

        input_i = text.split(f"Input {input_num}:")[-1]
        input_i = input_i.split(f"Output {input_num}:")[0].strip()

        all_input_list.append(input_i)
        input_num += 1

    for input_item in all_input_list:
        assert isinstance(input_item, str)

    return all_input_list


def extract_outputs(text: str) -> List[str]:
    """
    Given a string of a particular format, extracts
    all the outputs, and returns them.

    Input:
        text (str):
            Usually has the following format:
            "
            Input 1: ....
            Output 1: ....

            Input 2: ....
            Output 2: ....
            "

    Output:
        all_output_list (List[str]):
            List of all the outputs in the text string
    """
    output_num = 1
    all_output_list = []

    while True:
        if f"Output {output_num}:" not in text:
            break

        output_i = text.split(f"Output {output_num}:")[-1]
        if f"Input {output_num + 1}:" in output_i:
            output_i = output_i.split(f"Input {output_num + 1}:")[0].strip()

        all_output_list.append(output_i.strip())
        output_num += 1

    for output_item in all_output_list:
        assert isinstance(output_item, str)

    return all_output_list


def extract_automation_rule(text: str) -> Dict[str, str]:
    """
    Given a text of the following format:
        "<rule> 111: 1 </rule>\n<rule> 110: 2 </rule> ..."
    This function extracts the automation ruleset from
    this string.

    Input:
        text (str):
            Text that contains (most likely LLM generated)
            automation rule

    Output:
        automation_rule (Dict[str, str]):
            Extracted automation rule
    """
    neighborhoods = [
        "111",
        "110",
        "101",
        "100",
        "011",
        "010",
        "001",
        "000",
    ]

    automation_rule = {}
    for neighborhood in neighborhoods:
        assert neighborhood in text
        text_part = text.split(f"{neighborhood}:")[-1]

        assert "</rule>" in text_part
        next_cell_state = text_part.split("</rule>")[0].strip()

        assert len(next_cell_state) == 1
        automation_rule[neighborhood] = next_cell_state

    return automation_rule


class CellularAutomataEnv(BaseEnv):
    """
    This class contains the logic for generating feedback for the 
    Elementary 1D cellular automation task 
    (https://en.wikipedia.org/wiki/Elementary_cellular_automaton),
    given a guess of the transition rules 
    of cellular automation from provided inputs and outputs.
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
        assert "env" in task_state
        self.goal_state = deepcopy(task_state["env"])

        assert "agent" in task_state
        self.start_state = deepcopy(task_state["agent"])

        self.mode = mode
        assert self.mode in ["train", "test"]

        self.trajectory_level_reward = CELLULAR_AUTOMATA_DEFAULT_REWARD_FOR_UNSOLVED_TASK

    def get_start_state(self) -> str:
        return CELLULAR_AUTOMATA_ENV_DATA["agent"].format(
            agent=self.start_state,
        )
    
    def get_max_num_tokens_per_turn(self) -> Optional[int]:
        return 1024
        
    def get_max_turns(self) -> int:
        return CELLULAR_AUTOMATA_ENV_DATA["max_turns"]
    
    def get_custom_system_prompt(
       self     
    ) -> str:
        return self.custom_system_prompt_str
    
    def get_default_system_prompt(self) -> str:
        return self.default_system_prompt_str
    
    def get_system_prompt(self) -> str:
        return self.default_system_prompt_str

    def step(
        self,
        conversation_history: List[Dict[str, str]],
    ) -> Dict[str, Union[str, bool]]:
        self.validate_conversation_history(
            conversation_history=conversation_history,
        )

        # Preliminary checks on the conversation_history
        assert len(conversation_history) >= 2

        # Extract agent generation
        assert conversation_history[-1]["role"] == "assistant"
        last_assistant_response = conversation_history[-1]["content"]

        try:
            automation_rule = extract_automation_rule(
                text=last_assistant_response,
            )
        except:
            return {
                "content": CELLULAR_AUTOMATA_ENV_DATA["environment_default_response"],
                "goal_reached": False,
                "judge_label": False,
            }

        # Extract example inputs and outputs
        all_input_list = extract_inputs(text=self.goal_state)
        all_true_output_list = extract_outputs(text=self.goal_state)
        assert len(all_input_list) == len(all_true_output_list)

        # generate outputs from the LLM predicted automation rule
        outputs_generated_by_given_automation_rule: List[str] = []
        for input_cell_state in all_input_list:
            output_cell_state = generate_next_state_1D_cellular_automatation(
                current_state=input_cell_state.split(), 
                automation_rule=automation_rule,
            )
            output_cell_state = " ".join(output_cell_state)
            outputs_generated_by_given_automation_rule.append(output_cell_state)
                
        goal_reached = True
        for index in range(len(all_true_output_list)):
            true_output = all_true_output_list[index]
            generated_output = outputs_generated_by_given_automation_rule[index]

            if true_output != generated_output:
                goal_reached = False
                break

        if goal_reached:
            feedback = "Goal reached"
            self.trajectory_level_reward = CELLULAR_AUTOMATA_DEFAULT_REWARD_FOR_SOLVED_TASK

        else:
            feedback = (
                "Sorry, the automation rule you guessed does not "
                "generate the correct outputs for all the given inputs. "
                "I will give you the outputs from the rules that you gave last time. "
                "Please use them to refine your guess about the automation rule."
            )

            for index in range(len(all_input_list)):
                feedback += f"\n\nInput {index + 1}: " + all_input_list[index]
                feedback += f"\nTrue Output {index + 1}: " + all_true_output_list[index]
                feedback += f"\nOutput generated by the last rule you gave: "
                feedback += outputs_generated_by_given_automation_rule[index]

            feedback += CELLULAR_AUTOMATA_ENV_DATA["agent_optional_message"]
        
        return {
            "content": feedback.strip(),
            "goal_reached": (feedback == "Goal reached"),
            "judge_label": (feedback == "Goal reached"),
        }
