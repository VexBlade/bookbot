import sys
from stats import (
     count_words,
     count_characters,
     count_characters_sorted
)

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_words = get_book_text(book_path)
    total_words = count_words(book_words)
    char_count = count_characters(book_words)
    sorted_char_count = count_characters_sorted(book_words)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("----------- Character Count ----------")
    
    # BEGIN: print_char_count
    for char, num in sorted_char_count.items():
        print(f"{char}: {num}")
    # END: print_char_count
    
    print("============= END ===============")

    

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text 

main()
