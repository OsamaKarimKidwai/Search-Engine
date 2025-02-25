# Simple Search Engine for MARX & ENGELS COLLECTED WORKS

The goal of this project is to develop a simple search engine that processes, tokenizes, and indexes the content of the book "MARX & ENGELS COLLECTED WORKS." The search engine aims to facilitate efficient retrieval of information within the text by creating an inverted index and providing a graphical user interface (GUI) for user interaction.

# Contributors
Zahra Alahmedi,          
Osama Karim Kidwai,      
Eric Rawlins

# Prerequisites

Before running the provided Python scripts and GUI, ensure you have the following prerequisites installed on your system:

### **Python:**

Make sure Python is installed on your system. You can download it from python.org.

### **Required Python Libraries:**

Install the necessary libraries using the following command:

pip install PyPDF2 nltk jellyfish

**NLTK Resources:**

After installing the nltk library, download the required resources by running in your terminal or script:

import nltk
nltk.download('punkt')                                                      
nltk.download('stopwords')

**GUI Library:**

Ensure that the Tkinter library is available. It is included in the standard Python library, so no additional installation is needed.
Note: Refer to the limiation Section for the Limitations of GUI.

# Usage and Configuration

To effectively use the Search Engine, follow these steps:

1- We are using a ready group of texts, please insure they are inside the file mybook, which should be in the same folder as well.

2- Run the script CS465_665_W24_IRproject_Group3_Inverted_index_with_input_and_soundex.py which will extract the distinct words, the distinct words and the posting list and save them to txt files in the main folder. It will give the option to input and search the word and also provide its Soundex code.

3- Run the script CS465_665_W24_IRproject_Group3_top_words.py.

4- Run the script CS465_665_W24_IRproject_Group3IR_GUI

5- Run the script CS465_665_W24_IRproject_Group3_all_words


To configure and execute the Marx & Engels Collected Works Search Engine:

**File replacement:**

Ensure the new pdf file is in the same folder.
Replace the file name in the main script:  pdf_path = 'CS465-665-W24-IRproject-Group#3-Marx & Engels Collected Works.pdf' with the new book name before running the main secript. You can replace the txt files in the folder mybook or add on them and you will not need to run the main.


# Results

Inverted Index: Generated and stored in inverted_index.txt.
Posting List: Created and saved in PostingLists_AllDocs.txt.
Distinct Words: 18,127 distinct words in the entire collection.
Total Words: 303,381 words in the entire collection.
Search Function: Provides the index and Soundex for the entered word.
Ranked Words: Displays ranks for the 100th, 500th, and 1000th words in the collection.
Distinct Words in each doc with the total number of words stored in distinct_words_in_each_doc.txt.
Persinak 



Added Soundex code


# References

1- Codex, A. C. (2023, July 25). How to Create a Simple Search Engine with Python. Reintech. https://reintech.io/blog/create-simple-search-engine-with-python. 
2- Christian Hur. (2023, March 20). Build a mini search engine in Python [Video]. YouTube. https://www.youtube.com/watch?v=TvI4xELvAn0.
3- Welcome to PyPDF2 — PyPDF2 documentation. (n.d.). https://pypdf2.readthedocs.io/en/3.0.0/
4-  Kaur, G. (2024, January 23). [Fix] “Cannot Set up Python SDK” Error in PyCharm with
Virtualenv after OS Reinstall - AskPython. AskPython. https://www.askpython.com/python/examples/cannot-setup-python-sdk-error-virtualenv
5- NLTK: Natural Language Toolkit. (n.d.). https://www.nltk.org/
6- GeeksforGeeks. (2023b, June 8). Python Collections Module. https://www.geeksforgeeks.org/python-collections-module/
7- 7- Mubashir2329. (2020, September 3). IR-Assignment1-inverted-Index. GitHub. https://github.com/mubashir2329/IR-Assignment1-inverted-index/blob/master/task1.py
8- Sarkar. (2018, March 15). Posting-lists-Information-Retrieval. GitHub. https://github.com/shreemoyee/posting-lists-Information-Retrieval-/blob/master/Assignment2_IR%20_Faster.py
9- GeeksforGeeks. (2023a, January 30). Create Inverted Index for File using Python. https://www.geeksforgeeks.org/create-inverted-index-for-file-using-python/
