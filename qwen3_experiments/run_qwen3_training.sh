conda activate maxrl


# ============ Ray Cluster Setup ============
# Getting the node names
ray stop --force

nodes=$(scontrol show hostnames "$SLURM_JOB_NODELIST")
nodes_array=($nodes)

head_node=${nodes_array[0]}
head_node_ip=$(srun --nodes=1 --ntasks=1 -w "$head_node" hostname --ip-address)

# if we detect a space character in the head node IP, we'll
# convert it to an ipv4 address. This step is optional.
if [[ "$head_node_ip" == *" "* ]]; then
    IFS=' ' read -ra ADDR <<<"$head_node_ip"
    if [[ ${#ADDR[0]} -gt 16 ]]; then
        head_node_ip=${ADDR[1]}
    else
        head_node_ip=${ADDR[0]}
    fi
    echo "IPV6 address detected. We split the IPV4 address as $head_node_ip"
fi

port=6379
ip_head=$head_node_ip:$port
export ip_head
echo "IP Head: $ip_head"

# Ray binary path
RAY_BIN=/path_to_ray/bin/ray

# Start Ray head node directly (script runs on head node)
echo "Starting HEAD on local node: $(hostname)"

unset ROCR_VISIBLE_DEVICES
export NCCL_DEBUG=INFO
export TORCH_NCCL_TRACE_BUFFER_SIZE=1048576
export RAY_TMPDIR=/tmp/ray


$RAY_BIN start --head \
    --node-ip-address="$head_node_ip" \
    --port=$port \
    --num-cpus "${SLURM_CPUS_PER_TASK}" \
    --num-gpus "${SLURM_GPUS_ON_NODE}"

echo "HEAD started, waiting..."
sleep 10

# Check if head is running
$RAY_BIN status
echo "Head node ready"

# Start Ray worker nodes via srun
worker_num=$((SLURM_JOB_NUM_NODES - 1))

for ((i = 1; i <= worker_num; i++)); do
    node_i=${nodes_array[$i]}
    echo "Starting WORKER $i at $node_i"

    srun --nodes=1 --ntasks=1 -w "$node_i" --export=ALL bash -c "
        unset ROCR_VISIBLE_DEVICES
        source /path/to/anaconda3/etc/profile.d/conda.sh
        conda activate paprika
        export NCCL_DEBUG=INFO
        export TORCH_NCCL_TRACE_BUFFER_SIZE=1048576
        export RAY_TMPDIR=/tmp/ray
        $RAY_BIN start --address \"$ip_head\" \
            --num-cpus ${SLURM_CPUS_PER_TASK} \
            --num-gpus ${SLURM_GPUS_ON_NODE}
    " &
    sleep 10
done

# Wait for Ray cluster to be ready
sleep 20
echo "Ray cluster started"
echo "ip_head=$ip_head"

# Check Ray status
$RAY_BIN status


export FULL_BATCH_SIZE=256
export PPO_MINI_BATCH_SIZE=256

# Number of rollouts
export NUM_PER_PROMPT_ROLLOUTS=16

# prompt and response length cutoff
export MAX_RESPONSE_LENGTH=4096
export MAX_PROMPT_LENGTH=1024

# Other hyperparameters
export LEARNING_RATE=1e-6

# RL with ground truth hyperparams
export REWARD_MANAGER='multi_thread'

####
# Change any hyperparams you need, by adding another line here
# For example, if you uncomment the following line
# LEARNING_RATE=3e-7
# the it will set the learning rate to 3e-7 instead of the default value

PER_GPU_MINI_BATCH_SIZE=4
NUM_PER_PROMPT_ROLLOUTS_VALIDATION=32
MAX_MODEL_LEN=32000
MAX_NUM_BATCHED_TOKENS=32000
MAX_TRAJECTORY_LENGTH=3900
TENSOR_MODEL_PARALLEL_SIZE=1

PPO_EPOCHS=1

CLIP_RATIO_LOW=0.2
CLIP_RATIO_HIGH=0.2
GRAD_CLIP=0.3

# KL coefficient (set to 0.0 since use_kl_loss=False)
KL_COEFF=0.0

echo "This is the per-GPU mini batch size: $PER_GPU_MINI_BATCH_SIZE"
echo "This is the Maximum response length: $MAX_RESPONSE_LENGTH"


TRAIN_DATASET_PATH=/path/to/polaris/train.parquet
TEST_DATASET_PATH="['/path/to/aime25/test.parquet','/path/to/math/test.parquet']"

TOTAL_EPOCHS=5

# Set model path
MODEL_PATH=Qwen/Qwen3-1.7B-Base
MODEL_NAME=Qwen3-1.7B-Base

# Uncomment the following two lines if we want to run Qwen3-4B-Base
# MODEL_PATH=Qwen/Qwen3-4B-Base
# MODEL_NAME=Qwen3-4B-Base

ADVANTAGE_ESTIMATOR=maxrl

# Uncomment the following line if we want to run GRPO
# ADVANTAGE_ESTIMATOR=grpo

PROJECT_NAME=Qwen3_MaxRL_Experiments
EXPERIMENT_NAME=${ADVANTAGE_ESTIMATOR}_${MODEL_NAME}


CHECKPOINT_SAVE_PATH=/path/to/checkpoints/${PROJECT_NAME}/${EXPERIMENT_NAME}

export VLLM_ATTENTION_BACKEND=FLASH_ATTN
export SEED=79
export NCCL_DEBUG=INFO
export TORCH_NCCL_TRACE_BUFFER_SIZE=1048576

export NCCL_ALGO=RING
export NCCL_IB_AR_THRESHOLD=0
export NCCL_IB_PCI_RELAXED_ORDERING=1
export NCCL_IB_SPLIT_DATA_ON_QPS=0
export NCCL_IB_QPS_PER_CONNECTION=2
export UCX_IB_PCI_RELAXED_ORDERING=on
export CUDA_DEVICE_ORDER=PCI_BUS_ID
export NCCL_SOCKET_IFNAME=eth0
export NCCL_IB_HCA=$(
    for dev in $(ls -d /sys/class/infiniband/mlx5_* | sort -V); do
        name=$(basename $dev)
        link=$(cat $dev/ports/1/link_layer 2>/dev/null)
        if [[ "$link" == "InfiniBand" ]]; then
            pcie=$(basename $(readlink -f $dev/device))
            echo "$pcie $name"
        fi
    done | sort | awk '{print $2":1"}' | paste -sd,
)
export UCX_NET_DEVICES=eth0
export NCCL_IGNORE_CPU_AFFINITY=1

python3 -W ignore -m verl.trainer.main_ppo \
    algorithm.adv_estimator=$ADVANTAGE_ESTIMATOR \
    data.train_files=$TRAIN_DATASET_PATH \
    data.val_files=$TEST_DATASET_PATH \
    data.train_batch_size=$FULL_BATCH_SIZE \
    data.max_prompt_length=$MAX_PROMPT_LENGTH \
    data.max_response_length=$MAX_RESPONSE_LENGTH \
    data.filter_overlong_prompts=True \
    data.truncation='error' \
    actor_rollout_ref.model.path=$MODEL_PATH \
    actor_rollout_ref.actor.optim.lr=$LEARNING_RATE \
    actor_rollout_ref.model.use_remove_padding=True \
    actor_rollout_ref.actor.ppo_mini_batch_size=$PPO_MINI_BATCH_SIZE \
    actor_rollout_ref.actor.ppo_micro_batch_size_per_gpu=$PER_GPU_MINI_BATCH_SIZE \
    actor_rollout_ref.actor.use_kl_loss=False \
    actor_rollout_ref.actor.kl_loss_coef=$KL_COEFF \
    actor_rollout_ref.actor.clip_ratio_low=$CLIP_RATIO_LOW \
    actor_rollout_ref.actor.clip_ratio_high=$CLIP_RATIO_HIGH \
    actor_rollout_ref.actor.grad_clip=$GRAD_CLIP \
    actor_rollout_ref.model.enable_gradient_checkpointing=True \
    actor_rollout_ref.actor.fsdp_config.param_offload=False \
    actor_rollout_ref.actor.fsdp_config.optimizer_offload=False \
    actor_rollout_ref.actor.ppo_epochs=$PPO_EPOCHS \
    actor_rollout_ref.rollout.log_prob_micro_batch_size_per_gpu=$PER_GPU_MINI_BATCH_SIZE \
    actor_rollout_ref.rollout.tensor_model_parallel_size=$TENSOR_MODEL_PARALLEL_SIZE \
    actor_rollout_ref.rollout.name=vllm \
    actor_rollout_ref.rollout.max_model_len=$MAX_MODEL_LEN \
    actor_rollout_ref.rollout.max_num_batched_tokens=$MAX_NUM_BATCHED_TOKENS \
    actor_rollout_ref.rollout.gpu_memory_utilization=0.7 \
    actor_rollout_ref.rollout.n=$NUM_PER_PROMPT_ROLLOUTS \
    actor_rollout_ref.ref.log_prob_micro_batch_size_per_gpu=$PER_GPU_MINI_BATCH_SIZE \
    actor_rollout_ref.ref.fsdp_config.param_offload=True \
    actor_rollout_ref.rollout.val_kwargs.n=$NUM_PER_PROMPT_ROLLOUTS_VALIDATION \
    actor_rollout_ref.rollout.val_kwargs.do_sample=True \
    actor_rollout_ref.rollout.val_kwargs.temperature=0.6 \
    actor_rollout_ref.rollout.val_kwargs.top_p=0.95 \
    actor_rollout_ref.rollout.val_kwargs.top_k=-1 \
    actor_rollout_ref.rollout.multi_turn.enable=False \
    algorithm.use_kl_in_reward=False \
    algorithm.kl_penalty=low_var_kl \
    algorithm.kl_ctrl.kl_coef=$KL_COEFF \
    reward_model.reward_manager=$REWARD_MANAGER \
    trainer.balance_batch=True \
    trainer.critic_warmup=0 \
    trainer.val_before_train=True \
    trainer.val_only=False \
    trainer.val_on_last_step=True \
    trainer.logger=['console','wandb'] \
    trainer.project_name=$PROJECT_NAME \
    trainer.experiment_name=$EXPERIMENT_NAME \
    trainer.default_local_dir=$CHECKPOINT_SAVE_PATH \
    trainer.n_gpus_per_node=8  \
    trainer.nnodes=4 \
    trainer.save_freq=50 \
    trainer.max_actor_ckpt_to_keep=400 \
    trainer.max_critic_ckpt_to_keep=400 \
    trainer.test_freq=50 \
    trainer.total_epochs=$TOTAL_EPOCHS \
    ray_init.ray_dir=/tmp/ray $@