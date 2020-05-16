
#We are importing our datalayer insert, so we can insert into our database
from DataLayer import authors

#We are instantiating our class/object Author. So we can make an object later and set the properties, then insert them.
class Author:

    #The init defines all of the properties we can set
    def __init__(self):

        #Here are our properties
        self.id = None
        self.name = None

    #This is the way to add our property along with a way to set them, and get them!
    @property
    def id(self):
        return self.id
    @id.setter
    def id(self, value):
        self.id = value
    @id.deleter
    def id(self):
        del self.id
    
    #This is our instantiation of name, like we instantiated the id.
    @property
    def name(self):
        return self.name
    @name.setter
    def name(self, value):
        self.name = value
    @name.deleter
    def name(self):
        del self.name

    #This is our insert, where we can add some extra logic to make sure we have all the data we want, and in the right format.
    def insert(self, conn):
        #Check for data issues here

        #Here we are jumping into the datalayer to add our object to the database.
        authors.insert(self, conn)

