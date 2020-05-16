
#This is a function set up to insert our data directly into the datbase.
def insert(self, conn):

    #Here we are setting up a string that is SQL to insert our data.
    query = "insert into authors (name)"

    #I used some string interpolation along with our session variable self to set up our data.
    query += "values ('%s');" % (self.name)
    
    #Lets execute our query and set the data in the database.
    conn.execute(query)