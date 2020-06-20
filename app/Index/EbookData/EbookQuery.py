
#Import the library to look through our ebooks
from ebooklib import epub

#import using the operating system to find the path our file is currently in
import os

#Function to read our epub file 
def readEpub():

    #Set up our string of information to return
    returnData = ''

    #Load up our book to check for metadata
    book = epub.read_epub(os.path.dirname(os.path.abspath(__file__)) + '\Chronicles_Vol_1.epub')
    
    #Check title of the ebook and add it to our return data 
    for item in (book.get_metadata('DC', 'title')):
        returnData = item[0] + " "

    #Check the publisher of the ebook and add it to our return data 
    for item in (book.get_metadata('DC', 'publisher')):
        returnData += item[0] + " "

    #Check the publish date of the ebook and add it to our return data 
    for item in (book.get_metadata('DC', 'date')):
        returnData += item[0].split("-")[0] + " "

    #Check the author of the ebook and add it to our return data 
    for item in (book.get_metadata('DC', 'creator')):
        returnData += item[0]

    #Print our return data for sanity checking
    print(returnData)

    #Return our data
    return returnData