
def main():
    path = 'books/frankenstein.txt'
    text = get_book_text(path)
    print(text)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


main()