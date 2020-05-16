
#This is getting our function to insert the data into the database.
from DataLayer import books

#This is the instantiation of our book class so we can have an object to set our data in.
class Book:

    #Here is how we set all of our properties for our book
    def __init__(self):
        self.bookID = None
        self.title = None
        self.releaseDate = None
        self.pages = None
        self.authorID = None

    #Here is a quick function to see if one book is the same as another by looking at their bookID.
    def equals(self, other):
        return self.bookID == other.bookID

    #Here is where we can add logic to make sure we have all the data we want and that it is in the right format.
    def insert(self, conn):
        #Check for data issues here
        
        #Here we finally insert the data for our book.
        books.insert(self, conn)
