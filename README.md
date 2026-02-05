<div align="center">

# Maximum Likelihood Reinforcement Learning

</div>

This is the official PyTorch implementation of our paper "<strong>Maximum Likelihood Reinforcement Learning</strong>" by Fahim Tajwar*, Guanning Zeng*, Yueer Zhou, Yuda Song, Daman Arora, Yiding Jiang, Jeff Schneider, Ruslan Salakhutdinov, Haiwen Feng, and Andrea Zanette.

<div align="center">
<a href="https://zanette-labs.github.io/MaxRL/">
    <img src="https://img.shields.io/badge/Website-%231e37ff?style=for-the-badge"></a>
<a href="https://arxiv.org/abs/2602.02710">
    <img src="https://img.shields.io/badge/Paper-%23FF2442?style=for-the-badge"></a>
<a href="https://github.com/tajwarfahim/maxrl">
    <img src="https://img.shields.io/badge/Code-%2300CC00?style=for-the-badge"></a>
</div>

For any questions related to the codebase, please reach out to [Fahim Tajwar](mailto:tajwarfahim932@gmail.com) or [Guanning Zeng](mailto:zgn0303@gmail.com).

## Installation

In order for the installations to go smoothly, make sure you are operating from a GPU machine, typically one compatible with flash attention. It is ideal if you use the same GPU machines that you would use to run your experiments. 

Our installation mirrors that of setting up [verl](https://github.com/verl-project/verl). In particular, follow the steps below to ensure exact match with our environment setting.

First, create a fresh conda environment

```
conda create -n maxrl python==3.10
conda activate maxrl
```

Next, install pytorch and associated dependencies. In particular, we use the following version:

```
pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu124
```

Now we should install flash-attention. To do this smoothly, we will build it from source, but feel free to use any other method of choice as long as it works. 

Run the following commands one by one (we can change MAX_JOBS based on how much CPU memory and cores we have):

```
pip install ninja
pip install packaging
pip install psutil

git clone https://github.com/Dao-AILab/flash-attention.git
cd flash-attention
export MAX_JOBS=4
python setup.py install
```

Next, setup vllm.

```
pip install vllm==0.8.4
```

Setup additional things like wandb and math-verify.

```
pip install wandb
pip install math-verify
```

Now setup our codebase. Make sure you are inside the project folder, and run

```
pip install -e .
```

This should finish necessary installations. Note that it is possible that different packages may end up breaking since package versions keep changing, please your own judgement to fix them/reach out to us in case the above setup process leads to error. Thanks!

## Reproducing our experiments

### SmolLM on GSM8k

1. Download and preprocess data, change the local path appropriately according to your machine.

```
python examples/maxrl_data_preprocess/gsm8k.py --local_dir /path/to/gsm8k
```

2. Setup path configurations in `smollm/smollm.sh` 

3. `bash smollm/smollm.sh`

### 17x17 Maze

1. Download preprocessed data

```
huggingface-cli download guanning-ai/maze_17x17_1m --repo-type dataset --local-dir ./maze/data/
```

2. Setup path configurations in `maze/maze_17.sh`

3. `bash maze/maze_17.sh`

### ImageNet experiments

1. Install `hf-transfer` to be able to efficiently download the ImageNet-256x256 dataset.

```
pip install hf-transfer
pip install huggingface_hub
```

2. Run the following script after modifying it as you see fit.

```
bash imagenet/imagenet_training_script.sh
```

### Qwen3-1.7B-Base and Qwen3-4B-Base experiments

1. Download and preprocess all the datasets. Change the local file paths depending on your machine.

```
# Training dataset
python examples/maxrl_data_preprocess/polaris.py --local_dir /path/to/polaris

# Evaluation dataset
python examples/maxrl_data_preprocess/aime25.py --local_dir /path/to/aime25
python examples/maxrl_data_preprocess/beyondaime.py --local_dir /path/to/beyondaime
python examples/maxrl_data_preprocess/math_500.py --local_dir /path/to/math_500
python examples/maxrl_data_preprocess/minerva.py --local_dir /path/to/minerva
```

2. Now run the following script (modify to run different algorithms/change local file paths appropriately):

```
bash qwen3_experiments/run_qwen3_training.sh
```

Note that we use 4 nodes of 8xH200 GPUs for our training runs, please change the hyperparameters (or system-specific environment variables) appropriately according to the number of GPUs available in your system.


## Acknowledgements
The codebase for the algorithm is built on top of [verl](https://github.com/verl-project/verl), and we express our gratitude to the authors of verl for providing us with an easy-to-work-with codebase!

## Citation

If you find this repository useful for your research, please consider citing our paper:

```
@misc{tajwar2026maximumlikelihoodreinforcementlearning,
      title={Maximum Likelihood Reinforcement Learning}, 
      author={Fahim Tajwar and Guanning Zeng and Yueer Zhou and Yuda Song and Daman Arora and Yiding Jiang and Jeff Schneider and Ruslan Salakhutdinov and Haiwen Feng and Andrea Zanette},
      year={2026},
      eprint={2602.02710},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2602.02710}, 
}
```