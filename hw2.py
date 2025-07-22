# Name: Carlos Amezian
# Directory ID: camezian@umd.edu
# Date: 10/14/2020
# Assignment: Homework 2


def remove_punctuation(words):
    """This function removes non-alphabetical characters from a string.


    Args:
        words (string): contains word with non-alphbetical characters

    Returns:
        String: the formated string with only alphabetical characters
    """
    finalwords = "".join([i for i in words if i.isalpha()])
    return finalwords.lower()

class Book:

    def __init__(self, path):
        """Opens files specified by path for reading.

        Args:
            path (file): file going to be read
        """        
        self.words = []   
        fl = open(path, mode="r", encoding="UTF-8") 
        for lines in fl:
             words = lines.split(" ")
             for x in words:
                 self.words.append(remove_punctuation(x))
        # with open(path, encoding="Latin-1") as foo:
        #     for lines in foo:
        #         words = lines.split(" ")
        #         for x in words:                    
        #             self.words.extend(remove_punctuation(words))

    def make_sets(self):
        """Returns set created from words

        Returns:
            set: set cr4eated from wordsa attribute
        """        
        return set(self.words)


class Bookshelf:

    def __init__(self):
        """Sets index attribute to epmy dictionary
        """        
        self.index = {}

    def add_books(self, text):
        """Function creates a book object from the path being passed in.

        Args:
            text (list): the name of the work that we are creating a book object for
        """        
        myBook = Book(text)        
        myBook_sets = myBook.make_sets()
        
        for k in myBook_sets:
            if k in self.index:
                continue
            else:
                self.index[k] = [text]

def main(library):
    """Creates an instance of bookshelf where strings are the paths

    Args:
        library (list): list of al the books in the directory and are tha paths
    """    
    my_bookshelf = Bookshelf()

    for books in library:
        my_bookshelf.add_books(books)

    print(my_bookshelf.index)
    print(len(my_bookshelf.index))

if __name__ == "__main__":
    

    library = ["alice_wonderland.txt", "don_quixote.txt", "frederick_douglass.txt",
               "iliad.txt", "peter_pan.txt", "pride_prejudice.txt", "republic.txt",
               "sherlock_holms.txt", "wizard_of_oz.txt"]
    main(library)



f= 0

while f <= 1000:
    print('lfjkdjkdgd')
    
    f+=1