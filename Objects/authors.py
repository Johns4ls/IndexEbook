
#We are importing our datalayer insert, so we can insert into our database
from DataLayer import authors

#We are instantiating our class/object Author. So we can make an object later and set the properties, then insert them.
class Author:

    #The init defines all of the properties we can set
    def __init__(self):

        #Here are our properties
        self.id = None
        self.name = None

    #This is our insert, where we can add some extra logic to make sure we have all the data we want, and in the right format.
    def insert(self, conn):
        #Check for data issues here

        #Here we are jumping into the datalayer to add our object to the database.
        authors.insert(self, conn)

