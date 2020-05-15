from DataLayer import books
class Book:
    def __init__(self):
        self.bookID = None
        self.title = None
        self.releaseDate = None
        self.pages = None
        self.authorID = None

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



    def equals(self, other):
        return self.bookID == other.bookID
    def insert(self, conn):
        #Check for data issues here
        
        books.insert(self, conn)
