""" 
Zahra Alahmedi
Osama Karim Kidwai
Eric Rawlins
CS465/665, W24
Project # 1


performance
- Creating an inverted index in Python - Code Review Stack Exchange
"""
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
import jellyfish

nltk.download('punkt')
nltk.download('stopwords')


def create_inverted_index(documents_folder, output_file):
    inverted_index = defaultdict(list)
    total_words_count = 0  # Variable to track the total number of words

    stop_words = set(stopwords.words('english'))

    with open(output_file, 'w', encoding='utf-8') as result_file:
        for filename in os.listdir(documents_folder):
            if filename.endswith(".txt"):
                file_path = os.path.join(documents_folder, filename)

                with open(file_path, 'r', encoding='utf-8') as file:
                    document_text = file.read().lower()
                    tokens = [word for word in word_tokenize(document_text) if word.isalpha() and word not in stop_words]

                    # Track distinct words in each document
                    distinct_words = set(tokens)

                    # Update the inverted index with terms and their positions
                    for position, term in enumerate(tokens):
                        inverted_index[term].append((filename, position))

                    # Print the number of distinct words and total words in each document
                    result_file.write(f"Document: {filename}\n")
                    result_file.write(f"Distinct Words: {len(distinct_words)}\n")
                    result_file.write(f"Total Words: {len(tokens)}\n")
                    result_file.write("--------------\n")

                    # Update the total word count
                    total_words_count += len(tokens)

        result_file.write(f"Total Number of Distinct Words: {len(inverted_index)}\n")
        result_file.write(f"Total Number of Words Encountered: {total_words_count}\n")

    return inverted_index


def save_inverted_index(inverted_index, output_file):
    sorted_terms = sorted(inverted_index.keys())

    with open(output_file, 'a', encoding='utf-8') as file:
        for term in sorted_terms:
            postings_list = inverted_index[term]
            postings_str = ",".join([f"{doc}:{pos}" for doc, pos in postings_list])
            file.write(f"{term}: {postings_str}\n")


def print_soundex(word):
    soundex = jellyfish.soundex(word)
    return(word, soundex)
    #print(f"Soundex code for '{word}': {soundex}")
    
def search_index(inverted_index, search_word):
    results = []
    if search_word in inverted_index:
        postings_list = inverted_index[search_word]
        #print(f"Inverted Index for '{search_word}':")
        for doc, pos in postings_list:
            results.append(f"Document: {doc}, Position: {pos}")
            #print(f"Document: {doc}, Position: {pos}")
    else:
        results.append(f"The word '{search_word}' is not found in the documents.")
    return results


if __name__ == "__main__":
    documents_folder = "mybook"
    output_file = "distinct_words_in_each_doc.txt"
    inverted_index = create_inverted_index(documents_folder, output_file)
    save_inverted_index(inverted_index, "inverted_index.txt")
    
    search_word = input("Enter the word you want to search for: ").strip().lower()
    
    if search_word in inverted_index:
        postings_list = inverted_index[search_word]
        print(f"Inverted Index for '{search_word}':")
        for doc, pos in postings_list:
            print(f"Document: {doc}, Position: {pos}")
    else:
        print(f"The word '{search_word}' is not found in the documents.")

    print_soundex(search_word)


