
#This gets our classes/objects we've created
from Objects.books import Book
from Objects.authors import Author

#This is our way to get the ID of our Author we insert
from Database import getLastID

#Here we are going to load some data into our database
def LoadFakeData(conn):

    #We are create the author object and setting it as author1
    author1 = Author()

    #Lets set the name of the author and insert it into the database
    author1.name = "JK Rowling"
    author1.insert(conn)

    #Lets create a new book as book1, and set it as harry potter
    book1 = Book()
    book1.title = "Harry Potter"
    book1.releaseDate = "2002"
    book1.pages = 500

    #Here we are getting the last inserted ID of the author, so that we can link them up with a Foreign Key
    book1.authorID = getLastID.getAuthorID(conn)

    #Lets insert our book
    book1.insert(conn)

def LoadData (conn, Ebook):

        #We are creating the author object and setting it as author1
    author1 = Author()

    #Our name sometimes comes back as a list. So try to get it out. Otherwise, just take the name.
    try:
        author1.name = Ebook["Authors"][0]
    except:
        author1.name = Ebook["Authors"]
    
    #Lets insert our author into the database
    author1.insert(conn)

    #Lets create a new book as book1
    book1 = Book()
    book1.title = Ebook['Title']
    book1.releaseDate = Ebook['Year']
    book1.pages = 0

    #Here we are getting the last inserted ID of the author, so that we can link them up with a Foreign Key
    book1.authorID = getLastID.getAuthorID(conn)

    #Lets insert our book
    book1.insert(conn)