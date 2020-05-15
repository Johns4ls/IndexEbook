#This imports the functions we need to interact with our database
import sqlite3
from sqlite3 import Error

""" This is a suite of utility tools to interact with our operating system including making files, and editing them. 
    In our case we are finding the path of our current file."""
import os 

#This imports our tables.py inside the Database folder.
import tables

""" This is our function to create a database connection and update the tables"""
def create_connection():
    #Here we get the path of our file and append our database name to it.
    db_file = os.path.dirname(os.path.abspath(__file__)) + "/books.db"
    #Here we instantiate our connection variable
    conn = None
    #Lets try to connect to the database, and update our tables.
    try:
        conn = sqlite3.connect(db_file)
        tables.update_tables(conn)
        return conn
    #If we error out, lets print the error we got.
    except Error as e:
        print(e)