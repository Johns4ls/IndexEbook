
#Here is our function to insert the book into the database.
def insert(self, conn):

    #Here we are setting up the string which is SQL.
    query = "insert into books (title, releaseDate, pages, authorID)"

    #I used string interpolation to add the data into the query
    query += "values ('%s', %s, %s, %s);" % (self.title, self.releaseDate, self.pages, self.authorID)

    #Lets print the query to make sure it is correct
    print(query)

    #Lets insert the data into the database.
    conn.execute(query)