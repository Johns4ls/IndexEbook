#This is our module/folder Database
from Database import database
import dataLoader

#This is how we set up to run an object oriented python program.
if __name__ == '__main__':
    
#Creates our database connection, along with creating/updating tables
    conn = database.create_connection()

#This loads our data into the database.
    dataLoader.LoadFakeData(conn)
