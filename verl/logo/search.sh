#!/bin/bash

# DATASETS=("cifar10" "cifar100")
# DEPTHS=(2 4 8)
# LOSSES=("cross_entropy" "p_normalization" "grpo")
# DATASETS=("cifar10" "cifar100")
DATASETS=("imagenet-1k-32x32")
# DEPTHS=(8 20 32)
DEPTHS=(32)
LOSSES=("cross_entropy" "p_normalization" "grpo")
# LOSSES=("cross_entropy")
# LOSSES=("p_normalization" "grpo")
# LOSSES=("cross_entropy")

# ROLLOUT_SIZES=(4 32 1024 32768)
ROLLOUT_SIZES=(131072)
BATCH_SIZES=(128)
LRS=(1e-3)
# IMAGENET_K=(30 100 300 1000)
IMAGENET_K=(5)

# Full grid search
for dataset in "${DATASETS[@]}"; do
  for depth in "${DEPTHS[@]}"; do
    for loss in "${LOSSES[@]}"; do
      for rollout in "${ROLLOUT_SIZES[@]}"; do
        for batch in "${BATCH_SIZES[@]}"; do
          for lr in "${LRS[@]}"; do
            for imagenet_k in "${IMAGENET_K[@]}"; do
              if [ "$dataset" == "imagenet-1k-32x32" ]; then
                echo "Submitting job: dataset=$dataset depth=$depth loss=$loss rollout=$rollout batch=$batch lr=$lr imagenet_k=$imagenet_k"

                sbatch train.slurm \
                  --loss_type $loss \
                  --rollout_size $rollout \
                  --batch_size $batch \
                  --lr $lr \
                  --depth $depth \
                  --dataset $dataset \
                  --imagenet_k $imagenet_k \
                  --scheduler "cosine"
              fi
            done

          done
        done
      done
    done
  done
done
