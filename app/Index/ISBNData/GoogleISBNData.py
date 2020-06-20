
#Import API for google books
import isbnlib

#Function to query google books with the information from our ebook
def query(Ebook):

    #Here is our function to check again google books api
    isbn = isbnlib.goom(Ebook)
    
    #Return the information we found
    return isbn
