from stats import count_words
def main():
    path = 'books/frankenstein.txt'
    text = get_book_text(path)
    number_of_words = count_words(text)
    print(f'Found {number_of_words} total words')

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


main()