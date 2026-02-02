# Copyright 2024 Bytedance Ltd. and/or its affiliates
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from collections import defaultdict

import torch

from verl import DataProto
from verl.workers.reward_manager import register
from verl.workers.reward_manager.naive import NaiveRewardManager


@register("paprika")
class PaprikaRewardManager(NaiveRewardManager):
    """The reward manager."""
    def __call__(self, data: DataProto, return_dict=False):
        """We will expand this function gradually based on the available datasets"""

        reward_tensor = torch.zeros_like(data.batch["responses"], dtype=torch.float32)
        reward_extra_info = defaultdict(list)

        num_last_eos_token = 0
        last_eos_token_has_loss = 0

        for i in range(len(data)):
            data_item = data[i]  # DataProtoItem

            prompt_ids = data_item.batch["prompts"]
            response_ids = data_item.batch["responses"]
            loss_mask = data_item.batch["loss_mask"]

            prompt_length = prompt_ids.shape[-1]
            valid_response_length = data_item.batch["attention_mask"][prompt_length:].sum()

            # extract reward
            score = data_item.non_tensor_batch["rewards"]

            if isinstance(score, dict):
                reward = score["score"]
                # Store the information including original reward
                for key, value in score.items():
                    reward_extra_info[key].append(value)
            else:
                reward = score

            reward_tensor[i, valid_response_length - 1] = reward

            has_eos_token = (self.tokenizer.eos_token_id in response_ids.tolist())
            if has_eos_token:
                num_last_eos_token += 1

                # NOTE: just a dummy check, only works for single turn tasks
                eos_token_index = response_ids.tolist().index(self.tokenizer.eos_token_id)
                if loss_mask[eos_token_index] == 1:
                    last_eos_token_has_loss += 1

        eos_token_rate = float(num_last_eos_token) / len(data)
        eos_token_loss_rate = float(last_eos_token_has_loss) / len(data)

        if return_dict:
            reward_extra_info["eos_token_rate"] = eos_token_rate
            reward_extra_info["eos_token_loss_rate"] = eos_token_loss_rate
            
            return {
                "reward_tensor": reward_tensor,
                "reward_extra_info": reward_extra_info,
            }
        else:
            return reward_tensor