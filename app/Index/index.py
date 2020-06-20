#This is our module/folder Database
from app.Index import dataLoader
from app.Index.ISBNData import GoogleISBNData
from app.Index.EbookData import EbookQuery, MobiQuery, PDFQuery
from app.Database import database, tables

def index():
    #Creates our database connection, along with creating/updating tables
    conn = database.create_connection()

    #This loads our data into the database.
    dataLoader.LoadFakeData(conn)

    #Get data from epub, check metadata against google books database, and then submit it to our database
    dataLoader.LoadData(conn, GoogleISBNData.query(EbookQuery.readEpub())[0])

    #Get data from mobi, check metadata against google books database, and then submit it to our database
    dataLoader.LoadData(conn, GoogleISBNData.query(MobiQuery.readMobi())[0])

    #Get data from PDF, check metadata against google books database, and then submit it to our database
    dataLoader.LoadData(conn, GoogleISBNData.query(PDFQuery.readPDF())[0])