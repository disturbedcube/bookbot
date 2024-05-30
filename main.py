def main():
    book_path ="books/frankenstein.txt"
    book_text = get_text(book_path)
    words_in_text = count_words(book_text)
    letters_in_text = count_letters(book_text)
    print(f"There are {words_in_text} words in the book found at the path: {book_path}, the number of iterations of each character is as follows: {letters_in_text}")
def get_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(book):
    words_in_book = book.split()
    return len(words_in_book)

def count_letters(book):
    letters ={}
    words = book.split()
    for word in words:
        for char in word:
            if char.lower().isalpha():
                if char.lower() in letters:
                    letters[char.lower()] += 1
                else:
                    letters[char.lower()] = 1
    return letters

main()