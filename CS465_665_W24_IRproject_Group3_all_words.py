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
from collections import defaultdict

# Download NLTK resources
nltk.download('punkt')

# Function to write distinct words in the inverted index file to a separate file
def write_distinct_words_to_file(inverted_index_file, output_file):
    # Read the inverted index file
    with open(inverted_index_file, 'r', encoding='utf-8') as file:
        # Extract all distinct terms from the file
        terms_set = set(line.split(":")[0].strip() for line in file.readlines())

        # Write all distinct terms to a separate file called "distinct-words.txt"
        with open(output_file, 'w', encoding='utf-8') as distinct_words_file:
            distinct_words_file.write("\n".join(sorted(terms_set)))

# Function to count occurrences of each word in a file and collect document IDs
def count_word_occurrences(file_path):
    word_counts = defaultdict(int)
    document_ids = defaultdict(list)

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        # Tokenize the content of the file
        tokens = [word for word in word_tokenize(file.read().lower()) if word.isalnum()]

        # Count occurrences of each word and collect document IDs
        for doc_id, word in enumerate(tokens):
            word_counts[word] += 1
            document_ids[word].append(doc_id)

    return word_counts, document_ids

# Function to get the total number of words in a file
def get_total_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        # Tokenize the content of the file
        tokens = [word for word in word_tokenize(file.read().lower()) if word.isalnum()]

    return len(tokens)
# Function to process all text files in a folder
def process_all_text_files(folder_path):
    word_occurrences_all_docs = defaultdict(int)
    document_ids_all_docs = defaultdict(list)

    # Iterate through all text files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)

            # Count occurrences of each word in the current text file
            word_occurrences, document_ids = count_word_occurrences(file_path)

            # Update the overall word occurrences and document IDs
            for word, count in word_occurrences.items():
                word_occurrences_all_docs[word] += count
                document_ids_all_docs[word].extend(document_ids[word])

    return word_occurrences_all_docs, document_ids_all_docs
# Function to generate a posting list for a term
def generate_posting_list(term, document_ids):
    return f"{term}: {', '.join(map(str, document_ids))}"

# Function to write posting lists to a file
def write_posting_lists_to_file(posting_lists, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for term, posting_list in posting_lists.items():
            file.write(posting_list + '\n')
    
def distinct_word_count(document_folder):
    word_occurrences_all_docs, document_ids_all_docs = process_all_text_files(document_folder)
    word_occurrences, document_ids = count_word_occurrences("distinct-words.txt")

    # Report the number of distinct words
    distinct_words_count = len(word_occurrences)
    #print("\nNumber of distinct words: {}".format(distinct_words_count))

    # Get the total number of words in the entire mybook collection
    total_words_collection = 0
    for filename in os.listdir(document_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(document_folder, filename)
            total_words_collection += get_total_words(file_path)

    ("Total number of words in the entire mybook collection: {}".format(total_words_collection))

    # Generate posting lists for each term
    posting_lists_all_docs = {term: generate_posting_list(term, ids) for term, ids in document_ids_all_docs.items()}
    # Write posting lists to a file called "PostingLists_AllDocs.txt"
    write_posting_lists_to_file(posting_lists_all_docs, "PostingLists_AllDocs.txt")
    return(total_words_collection, distinct_words_count)
        
# Entry point of the script
if __name__ == "__main__":
    # Specify the folder containing the documents
    documents_folder = "mybook"
    # Process all text files in the "mybook" folder

    # Write distinct words in the inverted index file to a separate file
    write_distinct_words_to_file("inverted_index.txt", "distinct-words.txt")
    distinct_word_count(documents_folder)

