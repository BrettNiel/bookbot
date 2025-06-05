
from stats import num_of_words
from stats import count_of_each_character

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    # print((get_book_text("books/frankenstein.txt")))
    print(f"{num_of_words(get_book_text("books/frankenstein.txt"))} words found in the document")
    print(count_of_each_character(get_book_text("books/frankenstein.txt")))
    
main()