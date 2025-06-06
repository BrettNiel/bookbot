
from stats import num_of_words
from stats import count_of_each_character
from stats import sorted_dict

book = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words(get_book_text(book))} total words")
    print("--------- Character Count -------")
    for item in sorted_dict(count_of_each_character(get_book_text(book))):
         if item['char'].isalpha():
             print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()