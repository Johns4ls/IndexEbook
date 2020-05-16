#This is our module/folder Database
from Database import database
import dataLoader
from ISBNData import GoogleISBNData
from EbookData import EbookQuery

#This is how we set up to run an object oriented python program.
if __name__ == '__main__':
    
#Creates our database connection, along with creating/updating tables
    conn = database.create_connection()

#This loads our data into the database.
    dataLoader.LoadFakeData(conn)

#Get data from ebook, and check metadata against google books database, and submit it to our database
    dataLoader.LoadData(conn, GoogleISBNData.query(EbookQuery.readEpub())[0])
    