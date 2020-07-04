
#This is a function set up to insert our data directly into the datbase.
def insert(self, conn):

    #Here we are setting up a string that is SQL to insert our data.
    query = "insert into authors (name) "

    #I used some string interpolation along with our session variable self to set up our data.
    query += """values ("%s");""" % (self.name)
    
    #Lets execute our query and set the data in the database.
    try:
        conn.execute(query)
    except Exception as e:
        print(query)
        print(e)

    #This has to be run to save the data.
    conn.commit()

def update(self, conn):
    #TODO
    Print("Unimplemented")
    
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

def search(self, conn):

    #Here we are setting up a string representation of the SQL.
    cur = conn.cursor()
    cur.execute(f"""Select * from Authors WHERE name LIKE "{self.name}";""")
    return cur.fetchone()

def exists(self, conn):
    isSame = False
    #Here we are setting up a string representation of the SQL.
    cur = conn.cursor()
    cur.execute(f"""Select * from Authors WHERE name LIKE "{self.name}";""")
    results = cur.fetchall()
    if(len(results) > 0):
        isSame = True
    return isSame
