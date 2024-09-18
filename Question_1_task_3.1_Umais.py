import csv
from collections import Counter
import re

def count_words_in_text(output_csv):
    # Open the text file and read content
    with open(output_csv, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Clean and tokenize the text
    words = re.findall(r'\b\w+\b', text.lower())  # Convert text to lowercase and extract words
    
    # Count occurrences of each word
    word_counts = Counter(words)
    
    # Get the top 30 most common words
    top_30 = word_counts.most_common(30)
    
    # Write the results to a CSV file
    with open('top_30_words.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Word', 'Count'])  # Header
        csvwriter.writerows(top_30)
    
    return top_30

# Usage Example
top_words = count_words_in_text('output_csv.txt')
print(top_words)