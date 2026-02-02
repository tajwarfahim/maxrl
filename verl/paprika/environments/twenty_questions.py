import os
import time
from typing import List, Dict, Union, Optional, Any
from copy import deepcopy
from openai import (
    OpenAIError,
    OpenAI,
)

from verl.paprika.environments.base_env import BaseEnv
from verl.paprika.environments.env_configs.twenty_questions_config import (
    TWENTY_QUESTIONS_ENV_DATA,
)

TWENTY_QUESTIONS_DEFAULT_REWARD_FOR_UNSOLVED_TASK = 0.0
TWENTY_QUESTIONS_DEFAULT_REWARD_FOR_SOLVED_TASK = 1.0


class TwentyQuestionsEnv(BaseEnv):
    custom_system_prompt_str = (
        "You are a helpful assistant."
    )
    default_system_prompt_str = "You are a helpful assistant."
    model_name = "gpt-4o-mini"

    API_RETRY_SLEEP = 10
    API_ERROR_OUTPUT = "$ERROR$"
    API_QUERY_SLEEP = 0.5
    API_MAX_RETRY = 5
    API_TIMEOUT = 20

    MAX_ENV_RETRY = 5
    
    ENV_MAX_TOKENS = 128
    ENV_TEMPERATURE = 0.0
    ENV_TOP_P = 1.0

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

        self.trajectory_level_reward = TWENTY_QUESTIONS_DEFAULT_REWARD_FOR_UNSOLVED_TASK

        # We use OpenAI models for this
        oai_api_key = os.getenv("OAI_KEY")
        assert oai_api_key is not None, f"No OpenAI API key is available."
        self.client = OpenAI(api_key=oai_api_key)

        # Start the environment thread
        self.env_conv: List[Dict[str, str]] = [
            {
                "role": "system",
                "content": TWENTY_QUESTIONS_ENV_DATA["env"].format(
                    agent=self.start_state,
                    env=self.goal_state,
                ),
            },
        ]

    def get_start_state(self) -> str:
        agent_user_prompt: str = TWENTY_QUESTIONS_ENV_DATA["agent"]
        return agent_user_prompt.format(agent=self.start_state)
    
    def get_max_num_tokens_per_turn(self) -> Optional[int]:
        return 128
        
    def get_max_turns(self) -> int:
        return TWENTY_QUESTIONS_ENV_DATA["max_turns"]
    
    def get_custom_system_prompt(
       self     
    ) -> str:
        return self.custom_system_prompt_str
    
    def get_default_system_prompt(self) -> str:
        return self.default_system_prompt_str
    
    def get_system_prompt(self) -> str:
        return self.default_system_prompt_str
    
    def _generate_from_openai_api(
        self,
        conv: List[Dict],
        max_n_tokens: int,
        temperature: float,
        top_p: float,
    ) -> str:
        output = self.API_ERROR_OUTPUT

        for _ in range(self.API_MAX_RETRY):
            try:
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=conv,
                    max_tokens=max_n_tokens,
                    temperature=temperature,
                    top_p=top_p,
                )

                output = response.choices[0].message.content
                break

            except OpenAIError as e:
                print(type(e), e)

            time.sleep(self.API_RETRY_SLEEP)

        return output
    
    def extract_env_response(
        self,
        env_feedback: str,
    ) -> Optional[str]:
        env_feedback = env_feedback.lower()

        if env_feedback in ["yes", "yes."]:
            return "Yes"
        
        elif env_feedback in ["no", "no."]:
            return "No"
        
        elif env_feedback in ["goal reached", "goal reached."]:
            return "Goal reached"
        
        else:
            return None
        
    def run_judge_verification(
        self,
        trajectory: List[Dict[str, Any]],
    ) -> bool:
        judge_prompt = "The conversation begins here: \n\n"
        num_turns_to_judge = min(2, len(trajectory))
        
        for i in range(
            len(trajectory) - num_turns_to_judge, 
            len(trajectory)
        ):
            role = trajectory[i]["role"]
            message = trajectory[i]["content"]

            if role == "assistant":
                judge_prompt += "Agent: "
                judge_prompt += message
                judge_prompt += "\n\n"

            else:
                # We ignore the system prompt
                continue

        judge_prompt += " (End of Agent Turn)\n\n"
        judge_prompt += TWENTY_QUESTIONS_ENV_DATA["judge_prompt_suffix"].format(
            agent=self.start_state,
            env=self.goal_state,
        )

        judge_conv: List[Dict[str, Any]] = [
            {
                "role": "system",
                "content": TWENTY_QUESTIONS_ENV_DATA["judge_prompt_agent"].format(
                    agent=self.start_state,
                    env=self.goal_state,
                ),
            },
            {
                "role": "user",
                "content": judge_prompt,
            }
        ]

        judge_response = self._generate_from_openai_api(
            conv=judge_conv,
            max_n_tokens=self.ENV_MAX_TOKENS,
            temperature=self.ENV_TEMPERATURE,
            top_p=self.ENV_TOP_P,
        ).strip()

        judge_label = (judge_response == "<VALID>")
        return judge_label

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

        # add this to the environment thread
        environment_input = (
            last_assistant_response 
            + TWENTY_QUESTIONS_ENV_DATA["env_optional_message"].format(
                agent=self.start_state,
                env=self.goal_state,
            )
        )

        self.env_conv.append(
            {
                "role": "user",
                "content": environment_input,
            }
        )

        extracted_env_feedback = None

        for _ in range(self.MAX_ENV_RETRY):
            env_response = self._generate_from_openai_api(
                conv=self.env_conv,
                max_n_tokens=self.ENV_MAX_TOKENS,
                temperature=self.ENV_TEMPERATURE,
                top_p=self.ENV_TOP_P,
            ).strip()

            extracted_env_feedback = self.extract_env_response(
                env_feedback=env_response,
            )

            if extracted_env_feedback is not None:
                break

        # Environment could not generate correct feedback
        # Even after K tries
        # we assume the agent output is malformed, 
        # and terminate the trajectory.
        if extracted_env_feedback is None:
            return {
                "content": TWENTY_QUESTIONS_ENV_DATA["environment_default_response"],
                "goal_reached": False,
                "judge_label": False,
            }
        
        # Got a valid env feedback

        # First step: append it to the conversation history OF THE ENVIRONMENT
        self.env_conv.append(
            {
                "role": "assistant",
                "content": extracted_env_feedback,
            }
        )

        # Second step: run separate judge
        judge_label = self.run_judge_verification(
            trajectory=conversation_history,
        )

        # Third step: see if env returned goal reached
        goal_reached = (extracted_env_feedback == "Goal reached")

        # set trajectory level reward
        if goal_reached and judge_label:
            self.trajectory_level_reward = TWENTY_QUESTIONS_DEFAULT_REWARD_FOR_SOLVED_TASK
        
        """
        NOTE: in offline paprika, judge label = judge_label
        Here we use a stricter measure, i.e.,
            judge_label = judge_label and goal_reached

        I.e., the response needs to pass both measures in order to
        get positive reward.

        On the other hand,
            goal_reached = goal_reached or judge_label

        So if any of these conditions are true, 
        we return goal_reached = True, and terminate the trajectory.
        """
        return {
            "content": extracted_env_feedback,
            "goal_reached": goal_reached or judge_label,
            "judge_label": goal_reached and judge_label,
        }