from stats import count_words,  get_unique_characters, sorted_list
import sys

def main():
    validation()
    path = sys.argv[1]
    text = get_book_text(path)
    number_of_words = count_words(text)
    each_character_dict = get_unique_characters(text)
    sorted_characters = sorted_list(each_character_dict)
    print_menu(path, number_of_words, sorted_characters)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def validation():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def print_menu(path, number_of_words, sorted_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")

    for item in sorted_characters:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
        else:
            continue
    
    print("============= END ===============")

main()