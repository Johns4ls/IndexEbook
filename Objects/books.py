
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
    #Here are the setters and getters for our properties.
    @property
    def bookID(self):
        return self.bookID
    @bookID.setter
    def bookID(self, value):
        self.bookID = value
    @bookID.deleter
    def bookID(self):
        del self.bookID

    @property
    def title(self):
        return self.title
    @title.setter
    def title(self, value):
        self.title = value
    @title.deleter
    def title(self):
        del self.title

    @property
    def releaseDate(self):
        return self.releaseDate
    @releaseDate.setter
    def releaseDate(self, value):
        self.releaseDate = value
    @releaseDate.deleter
    def releaseDate(self):
        del self.releaseDate

    @property
    def pages(self):
        return self.pages
    @pages.setter
    def pages(self, value):
        self.pages = value
    @pages.deleter
    def pages(self):
        del self.pages
            
    @property
    def authorID(self):
        return self.authorID
    @authorID.setter
    def authorID(self, value):
        self.authorID = value
    @authorID.deleter
    def authorID(self):
        del self.authorID


    #Here is a quick function to see if one book is the same as another by looking at their bookID.
    def equals(self, other):
        return self.bookID == other.bookID

    #Here is where we can add logic to make sure we have all the data we want and that it is in the right format.
    def insert(self, conn):
        #Check for data issues here
        
        #Here we finally insert the data for our book.
        books.insert(self, conn)
