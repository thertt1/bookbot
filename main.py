from stats import word_count
from stats import char_count
from stats import formatting
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    pass

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book = sys.argv[1]
    text = (get_book_text(book))
    print(f'======== BOOKBOT ======== \nAnalyzing book found at {book}...\n-------- Word Count --------')
    word_count(text)
    print("-------- Character Count --------")
    formatting(char_count(text))

main()