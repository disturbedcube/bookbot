def main():

    generate_report()
    
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

def sort_on(dict):

    return dict["value"]

def generate_report():

    book_path ="books/frankenstein.txt"
    book_text = get_text(book_path)
    words_in_text = count_words(book_text)
    letters_in_text = count_letters(book_text)
    list_of_characters = []
    for key in letters_in_text:
        list_of_characters.append({"key":key, "value":letters_in_text[key]})
    list_of_characters.sort(reverse=True,key=sort_on)

    print("Generating Report \n")
    print("--------------------------------------------")
    print(f"There are {words_in_text} words in the book found at the path: {book_path} \n")
    for dictionary in list_of_characters:
        print(f"The letter {dictionary["key"]} was found {dictionary["value"]} times. \n")
    print("--------------------------------------------")

    
main()