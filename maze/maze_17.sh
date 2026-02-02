#!/bin/bash
# Maze 17x17 Training Script

set -e

# ============ Configuration ============
MODEL_PATH=/path/to/maze_sft_model
TRAIN_DATA=/path/to/maze/train.parquet
VAL_DATA=/path/to/maze/test.parquet
CHECKPOINT_DIR=/path/to/ckpt-1500

# Training hyperparameters
ADVANTAGE_ESTIMATOR=maxrl
TRUNCATE_ORDER=64
LR=1e-4
N_ROLLOUTS=128
N_VAL=2048
TRAIN_BATCH_SIZE=256

PROJECT_NAME=MaxRL_Maze_17x17
EXPERIMENT_NAME=${ADVANTAGE_ESTIMATOR}_${N_ROLLOUTS}rollouts

# ============ Ray Setup ============
ray stop --force 2>/dev/null || true
ray start --head --num-gpus 4
ray status

# ============ Training ============
python3 -m verl.trainer.main_ppo \
  algorithm.adv_estimator=${ADVANTAGE_ESTIMATOR} \
  algorithm.use_kl_in_reward=False \
  algorithm.pass_k=4 \
  algorithm.truncate_order=${TRUNCATE_ORDER} \
  data.train_files=${TRAIN_DATA} \
  data.val_files=${VAL_DATA} \
  data.train_batch_size=${TRAIN_BATCH_SIZE} \
  data.max_prompt_length=320 \
  data.max_response_length=180 \
  data.apply_chat_template=False \
  actor_rollout_ref.model.path=${MODEL_PATH} \
  actor_rollout_ref.actor.optim.lr=${LR} \
  actor_rollout_ref.actor.use_kl_loss=False \
  actor_rollout_ref.actor.dtype=float16 \
  actor_rollout_ref.actor.ppo_mini_batch_size=${TRAIN_BATCH_SIZE} \
  actor_rollout_ref.actor.ppo_micro_batch_size_per_gpu=4096 \
  actor_rollout_ref.rollout.name=hf \
  +actor_rollout_ref.rollout.micro_batch_size=4096 \
  actor_rollout_ref.rollout.dtype=float16 \
  actor_rollout_ref.rollout.log_prob_micro_batch_size_per_gpu=4096 \
  actor_rollout_ref.rollout.tensor_model_parallel_size=1 \
  actor_rollout_ref.rollout.gpu_memory_utilization=0.7 \
  actor_rollout_ref.ref.log_prob_micro_batch_size_per_gpu=4096 \
  actor_rollout_ref.rollout.n=${N_ROLLOUTS} \
  actor_rollout_ref.rollout.val_kwargs.n=${N_VAL} \
  actor_rollout_ref.rollout.val_kwargs.do_sample=True \
  actor_rollout_ref.rollout.val_kwargs.temperature=1.0 \
  reward_model.reward_manager=prime \
  +reward_model.reward_kwargs.num_processes=64 \
  +reward_model.reward_kwargs.chunksize=64 \
  algorithm.kl_ctrl.kl_coef=0.0 \
  trainer.project_name=${PROJECT_NAME} \
  trainer.experiment_name=${EXPERIMENT_NAME} \
  trainer.logger=['console','wandb'] \
  trainer.val_before_train=True \
  trainer.n_gpus_per_node=4 \
  trainer.nnodes=1 \
  trainer.save_freq=250 \
  trainer.test_freq=250 \
  trainer.max_actor_ckpt_to_keep=300 \
  trainer.default_local_dir=${CHECKPOINT_DIR}/${PROJECT_NAME}/${EXPERIMENT_NAME} \
  trainer.total_epochs=10
