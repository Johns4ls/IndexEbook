
#Import our mobi parsing library
from mobi import Mobi

#Import os to get the current path of our file
import os

#Here is our function to parse out the data from the mobi file
def readMobi(eBook):

    #Open up our book and parse it 
    book = Mobi(eBook)
    book.parse()
    #Return the information we want
    return(book.title().decode("utf-8") + " " + book.author().decode("utf-8"))

