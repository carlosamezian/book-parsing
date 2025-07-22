# import os


def remove_punctuation(word):
    '''Removing the non alphanumeric characters and converting the string to the lower string'''
    alphanumeric_string = "".join(e for e in word if e.isalpha())
    alphanumeric_string = alphanumeric_string.lower()
    return alphanumeric_string


class Book:
    def __init__(self, path):
        '''Constructor to open the file and adding the word of the file to the words list'''
        self.words = []
        file = open(path, encoding="Latin-1")

        for line in file:
            line_words = line.split(" ")

            for word in line_words:
                self.words.append(remove_punctuation(word))

    def make_sets(self):
        ''' This method creates the set and removes the duplicate words present in the words list'''
        return set(self.words)


class Bookshelf:
    def __init__(self):
        self.index = {}

    def add_books(self, text):
        '''Adding the book to the BookShelf accepts the path of the book as first argument.
            makes the set of the words in the book and add it to the index attribute of the object'''

        book = Book(text)
        book_set = book.make_sets()

        for word in book_set:
            if word in self.index:
                continue

            else:
                self.index[word] = [text]

    def print_index(self):
        ''' printing the word along with the list of the books in which the word is present'''
        for i in self.index:
            print(i, " -> ", end=" ")
            for book in self.index[i]:
                print(book, end=" ")

    def print_index_length(self):
        '''printing the length of index'''
        print("length of index =>", len(self.index))


def main(Library):
    ''' Driver function that accepts the list of file in the Libray list'''
    book_shelf = Bookshelf()
    for book in Library:
        book_shelf.add_books(book)

    book_shelf.print_index()
    book_shelf.print_index_length()


if __name__ == "__main__":
    library = ["alice_wonderland.txt", "don_quixote.txt", "frederick_douglass.txt",
               "iliad.txt", "peter_pan.txt", "pride_prejudice.txt", "republic.txt",
               "sherlock_holms.txt", "wizard_of_oz.txt"]

    main("don_quixote.txt")
