"""
Script to create a test split from guanning-ai/gsm8k-metamath dataset.
Randomly samples 256 questions and creates a new test split.
"""

from datasets import load_dataset, DatasetDict
import random

# Set random seed for reproducibility
random.seed(42)

def main():
    # Load the dataset
    print("Loading dataset guanning-ai/gsm8k-metamath...")
    dataset = load_dataset("guanning-ai/gsm8k-metamath")
    
    print(f"Dataset structure: {dataset}")
    print(f"Available splits: {list(dataset.keys())}")
    
    # Get the main split (usually 'train')
    if 'train' in dataset:
        main_split = 'train'
    else:
        main_split = list(dataset.keys())[0]
    
    print(f"Using split: {main_split}")
    print(f"Total samples in {main_split}: {len(dataset[main_split])}")
    
    # Get all indices and shuffle them
    all_indices = list(range(len(dataset[main_split])))
    random.shuffle(all_indices)
    
    # Select 256 indices for test split
    test_indices = all_indices[:256]
    remaining_indices = all_indices[256:]
    
    print(f"Selecting {len(test_indices)} samples for test split")
    print(f"Remaining {len(remaining_indices)} samples in {main_split}")
    
    # Create new splits
    test_dataset = dataset[main_split].select(test_indices)
    new_train_dataset = dataset[main_split].select(remaining_indices)
    
    # Create new DatasetDict
    new_dataset = DatasetDict({
        'train': new_train_dataset,
        'test': test_dataset
    })
    
    print(f"\nNew dataset structure:")
    print(f"  train: {len(new_dataset['train'])} samples")
    print(f"  test: {len(new_dataset['test'])} samples")
    
    # Push to Hub
    print("\nPushing to Hugging Face Hub...")
    new_dataset.push_to_hub("guanning-ai/gsm8k-metamath")
    
    print("Done! Dataset has been updated with test split.")

if __name__ == "__main__":
    main()

