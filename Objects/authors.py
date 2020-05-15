from DataLayer import authors
class Author:

    def __init__(self):
        self.id = None
        self.name = None

    @property
    def id(self):
        return self.id
    @id.setter
    def id(self, value):
        self.id = value
    @id.deleter
    def id(self):
        del self.id

    @property
    def name(self):
        return self.name
    @name.setter
    def name(self, value):
        self.name = value
    @name.deleter
    def name(self):
        del self.name


    def insert(self, conn):
        #Check for data issues here
    
        authors.insert(self, conn)

