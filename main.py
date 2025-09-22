from stats import count_words,  get_unique_characters

def main():
    path = 'books/frankenstein.txt'
    text = get_book_text(path)
    number_of_words = count_words(text)
    print(f'Found {number_of_words} total words')
    each_character_dict = get_unique_characters(text)
    print(each_character_dict)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


main()