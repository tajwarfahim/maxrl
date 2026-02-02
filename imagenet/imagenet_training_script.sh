echo "Script started"
conda activate maxrl

export HF_HUB_HTTP_TIMEOUT=300
export HF_HUB_ENABLE_HF_TRANSFER=1

LEARNING_RATE=0.1
SEED=69
MAX_K=2048
LOSS_TYPE=reinforce_with_p_normalization

# Change this to change number of rollouts per example
NUM_ROLLOUTS=1024

# Uncomment the lines below if you would want to train with different objectives
# LOSS_TYPE=grpo
# LOSS_TYPE=cross_entropy
# LOSS_TYPE=reinforce_with_baseline

python -m verl.cifar10_experiments.sampling_based_rl_objective_experiments \
    --wandb \
    --no-amp \
    --lr $LEARNING_RATE \
    --batch-size 256 \
    --epochs 20 \
    --seed $SEED \
    --model-type resnet \
    --model-depth 50 \
    --data-dir /home/ftajwar/data/imagenet \
    --dataset-name imagenet256 \
    --checkpoint-dir /home/ftajwar/imagenet256_checkpoints/${LOSS_TYPE}_${NUM_ROLLOUTS} \
    --wandb_runname ${LOSS_TYPE}_${NUM_ROLLOUTS}_lr_${LEARNING_RATE} \
    --wandb-project imagenet256_reinforce_learning_rate_ablations \
    --eval_every_k 1000 \
    --advantage-type $LOSS_TYPE \
    --max-k $MAX_K \
    --num_train_rollouts_per_example $NUM_ROLLOUTS \