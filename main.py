## open the book file
def get_book_text(path):
    with open(path)as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)

def main():
    bookpath = "books/frankenstein.txt"
    text = get_book_text(bookpath)
    num_words = get_num_words(text)
    print(num_words)

main()

# books\frankenstein.txt