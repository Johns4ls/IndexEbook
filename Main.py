#This is our module/folder Database
from Database import database
import dataLoader
from ISBNData import GoogleISBNData
from EbookData import EbookQuery, MobiQuery

#This is how we set up to run an object oriented python program.
if __name__ == '__main__':
    
#Creates our database connection, along with creating/updating tables
    conn = database.create_connection()

#This loads our data into the database.
    dataLoader.LoadFakeData(conn)

#Get data from epub, check metadata against google books database, and then submit it to our database
    dataLoader.LoadData(conn, GoogleISBNData.query(EbookQuery.readEpub())[0])
    
#Get data from mobi, check metadata against google books database, and then submit it to our database
    dataLoader.LoadData(conn, GoogleISBNData.query(MobiQuery.parseMobi())[0])