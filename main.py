from stats import get_num_words, get_char_frequency, sort_dictionary
import sys

def get_book_text(path_to_file) -> str:
    print(f"Analyzing book found at {path_to_file}...")
    with open(path_to_file, "r", encoding='utf-8') as f:
        return f.read()


def main():
    directories = sys.argv
    if len(directories) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book = get_book_text(directories[1])
    
    print("----------- Word Count ----------")
    num_words = get_num_words(book)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    sorted_char_frequency = sort_dictionary(get_char_frequency(book))
    for item in sorted_char_frequency:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()