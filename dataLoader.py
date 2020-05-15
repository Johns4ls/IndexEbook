from Objects.books import Book
from Objects.authors import Author
from Database import getLastID
def LoadFakeData(conn):
    author1 = Author()
    author1.name = "JK Rowling"
    author1.insert(conn)
    book1 = Book()
    book1.title = "Harry Potter"
    book1.releaseDate = "2002"
    book1.pages = 500
    book1.authorID = getLastID.getAuthorID(conn)
    book1.insert(conn)