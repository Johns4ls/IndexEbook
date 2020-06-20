
#We are importing our datalayer insert, so we can insert into our database
from app.DataLayer import authors

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
        if(self.name == None):
            return "An author must have a name", 500
        #Here we are jumping into the datalayer to add our object to the database.
        authors.insert(self, conn)

    def update(self, conn):
        #Check for data issues here
        if(self.authorID == None):
            return "An author must have an ID", 500
        #Here we update the data for our author.
        authors.update(self, conn)

    def delete(self, conn):
        #Check for data issues here
        if(self.authorID == None):
            return "An author must have an ID", 500
        #Here we delete the data for our author.
        authors.delete(self, conn)

    def findFromKey(conn, authorID):
        #Check for data issues here
        if (authorID == None):
            return "authorID cannot be None", 500
        #Lets try to find a author with the ID and return it
        return authors.findFromKey(conn, authorID)

    def findFromKeys(conn, authorIDs):
        #Check for data issues here
        if (authorID == None):
            return "authorID cannot be None", 500
        #Lets try to find a author with the ID and return it
        return authors.findFromKeys(conn, authorIDs)

    def findAll(conn):
        #Check for data issues here

        #Lets return all authors to the user
        return authors.findAll(conn)

    def search(conn, info):
        #Check for data issues here
        if(info is None):
            return "We cannot search for nothing", 500
        #Lets return all the authors we find
        return authors.search(conn, info)