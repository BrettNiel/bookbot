
from stats import num_of_words
from stats import count_of_each_character
from stats import sorted_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words(get_book_text(sys.argv[1]))} total words")
    print("--------- Character Count -------")
    for item in sorted_dict(count_of_each_character(get_book_text(sys.argv[1]))):
         if item['char'].isalpha():
             print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()