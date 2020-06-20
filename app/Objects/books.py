
#This is getting our function to insert the data into the database.
from app.DataLayer import books
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
        if(self.title is None):
            return "A book must have a title", 500
        if(self.authorID == None):
            return "A book must have an author", 500
        #Here we finally insert the data for our book.
        books.insert(self, conn)

    def update(self, conn):
        #Check for data issues here
        if(self.bookID is None):
            return "A book must have an ID", 500
        #Here we finally insert the data for our book.
        books.update(self, conn)

    def deleteFromKey(conn, bookID):
        #Check for data issues here
        if(bookID is None):
            return "A book must have an ID", 500
        #Here we finally insert the data for our book.
        books.deleteFromKey(conn, bookID)
    
    def findFromKey(conn, bookID):
        #Check for data issues here
        if(bookID is None):
            return "A book must have an ID", 500
        #Lets try to find a book with the ID and return it
        return books.findFromKey(conn, bookID)

    def findFromKeys(conn, bookIDs):
        #Check for data issues here
        if(bookIDs is None):
            return "A book must have an ID", 500
        #Lets try to find a book with the ID and return it
        return books.findFromKeys(conn, bookIDs)

    def findAll(conn):
        #Check for data issues here

        #Lets return all books to the user
        return books.findAll(conn)

    def search(conn, info):
        #Check for data issues here
        if(info is None):
            return "We cannot search for nothing", 500
        #Lets return all the books we find
        return books.search(conn, info)

    def searchTitle(conn, info):
        #Check for data issues here
        if(info is None):
            return "We cannot search for nothing", 500
        #Lets return all the books we find
        return books.searchTitle(conn, info)