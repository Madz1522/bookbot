
import sys
from stats import word_count, count_char, sort_char_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    text = get_book_text(path)
    count_words = word_count(text)
    count_character = count_char(text)
    sorted_character = sort_char_dict(count_character)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words} total words")
    print("--------- Character Count -------")
    for item in sorted_character:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()


