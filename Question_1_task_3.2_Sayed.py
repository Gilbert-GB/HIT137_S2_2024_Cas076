from transformers import AutoTokenizer
from collections import Counter

def count_unique_tokens(file_path, model_name='bert-base-uncased'):
    # Load the AutoTokenizer from Hugging Face
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # Open and read the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text
    tokens = tokenizer.tokenize(text.lower())  # Lowercase the text and tokenize
    
    # Count the occurrences of each token
    token_counts = Counter(tokens)
    
    # Get the top 30 most common tokens
    top_30_tokens = token_counts.most_common(30)
    
    # Print the top 30 tokens
    print("Top 30 most common tokens:")
    for token, count in top_30_tokens:
        print(f"{token}: {count}")
    
    return top_30_tokens

# Usage example:
file_path = 'CSV1.txt'  # Replace with the path to your .txt file
top_tokens = count_unique_tokens(file_path)