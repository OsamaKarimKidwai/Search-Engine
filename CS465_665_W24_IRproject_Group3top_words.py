""" 
Zahra Alahmedi
Osama Karim Kidwai
Eric Rawlins
CS465/665, W24
Project # 1
"""
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict


# Function to iterate through all txt files in a folder and count word occurrences
def count_word_occurrences_in_folder(mybook):
    word_counts = defaultdict(int)

    # Iterate through all txt files in the folder
    for filename in os.listdir(mybook):
        if filename.endswith(".txt"):
            file_path = os.path.join(mybook, filename)

            # Count occurrences of each word in the file
            with open(file_path, 'r', encoding='utf-8') as file:
                tokens = [word for word in word_tokenize(file.read().lower()) if word.isalnum()]
                for word in tokens:
                    word_counts[word] += 1

    return word_counts

# Entry point of the script
if __name__ == "__main__":
    # Specify the folder containing the documents
    documents_folder = "mybook"

    # Count occurrences of each word in all txt files in the folder
    word_occurrences = count_word_occurrences_in_folder(documents_folder)

    # Report the top 100th, 500th, and 1000th most-frequent words and their frequencies
    top_words = sorted(word_occurrences.items(), key=lambda x: x[1], reverse=True)

    for rank, (word, frequency) in enumerate(top_words, start=1):
        if rank in [100, 500, 1000]:
            print(f"Rank {rank}: {word} - Frequency: {frequency}")
