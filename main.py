
def main():
    path = 'books/frankenstein.txt'
    text = get_book_text(path)
    number_of_words = count_words(text)
    print(f'{number_of_words} words found in the document')

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def count_words(text_to_count):
    words_number = text_to_count.split()
    return len(words_number)

main()