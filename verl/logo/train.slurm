#!/bin/bash
#SBATCH --job-name=cifar
#SBATCH --output=logs/%j.out
#SBATCH --error=logs/%j.err
#SBATCH --time=00:30:00
#SBATCH --partition=general
#SBATCH --gres=gpu:A6000:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G

# Initialize module system
source /usr/share/Modules/init/bash
cd /home/damana
source .bashrc
conda activate ddp
cd /home/damana/logp

# Forward ALL arguments passed to this script into python
python train.py "$@"
