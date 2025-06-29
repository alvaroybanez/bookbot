import sys
from stats import word_count, letter_count, sorted_letter_count

def get_book_text(book_path):
    try:
        with open(book_path) as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file {book_path} was not found.")
        sys.exit(1)
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"------------ Word Count ------------")
    print(f"Found {word_count(book_text)} total words")
    print(f"------------ Character Count ------------")
    print(f"Found {len(letter_count(book_text))} unique characters")
    print(sorted_letter_count(letter_count(book_text)))
    print(f"============= END ===============")


if __name__ == "__main__":
    main()