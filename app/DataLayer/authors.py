
#This is a function set up to insert our data directly into the datbase.
def insert(self, conn):

    #Here we are setting up a string that is SQL to insert our data.
    query = "insert into authors (name) "

    #I used some string interpolation along with our session variable self to set up our data.
    query += "values ('%s');" % (self.name)
    
    #Lets execute our query and set the data in the database.
    conn.execute(query)

    #This has to be run to save the data.
    conn.commit()

def update(self, conn):
    #TODO
    
def deleteFromKey(conn, authorID):

    #Here we are setting up a string representation of the SQL.
    conn.execute(f"Delete from authors where authorID = {authorID}")

def findFromKey(conn, authorID):

    #Here we are setting up a string representation of the SQL.
    conn.execute(f"Select * from authors where authorID = {authorID}")
    cur = conn.cursor()
    return cur.fetchall()

def findFromKeys(conn, authorIDs):

    #Here we are setting up a string representation of the SQL.
    conn.execute(f"Select * from authors where authorID in {authorIDs}")
    cur = conn.cursor()
    return cur.fetchall()

def findAll(conn):

    #Here we are setting up a string representation of the SQL.
    cur = conn.cursor()
    cur.execute("Select * from authors;")
    return cur.fetchall()

def search(conn, info):

    #Here we are setting up a string representation of the SQL.
    cur = conn.cursor()
    cur.execute(f"Select * from Authors WHERE name LIKE '{info}'';")
    return cur.fetchall()
