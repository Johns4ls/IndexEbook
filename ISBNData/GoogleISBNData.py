
#Import API for google books
import isbnlib

#Function to query google books with the information from our ebook
def query(Ebook):
    isbn = isbnlib.goom(Ebook)

    #Return the information we found
    return isbn
