
#Here is our function to insert the book into the database.
def insert(self, conn):

    #Here we are setting up the string which is SQL.
    query = "insert into books (title, releaseDate, pages, authorID)"

    #I used string interpolation to add the data into the query
    query += """values ("%s", %s, %s, %s);""" % (self.title, self.releaseDate, self.pages, self.authorID)

    #Lets insert the data into the database.
    try:
        conn.execute(query)
    except Exception as e:
        print(query)
        print(e)

    #This has to be run to save the data.
    conn.commit()

def update(self, conn):
    #TODO
    print("Unimplemented")

def deleteFromKey(conn, bookID):

    #Here we are setting up a string representation of the SQL.
    conn.execute(f"Delete from books where bookID = {bookID}")

def findFromKey(conn, bookID):

    #Here we are setting up a string representation of the SQL.
    cur = conn.cursor()
    cur.execute(f"Select * from books where bookID = '{bookID}'")
    return cur.fetchall()

def findFromKeys(conn, bookIDs):

    #Here we are setting up a string representation of the SQL.
    cur = conn.cursor()
    cur.execute(f"Select * from books where bookID = {bookIDs}")
    return cur.fetchall()

def findAll(conn):

    #Here we are setting up a string representation of the SQL.
    cur = conn.cursor()
    cur.execute("Select * from books;")
    return cur.fetchall()

def searchTitle(conn, info):

    #Here we are setting up a string representation of the SQL.
    cur = conn.cursor()
    cur.execute(f"""Select * from books WHERE title LIKE "%{info}%";""")
    return cur.fetchall()

def exists(self, conn):

    #Here we are setting up a string representation of the SQL.
    isSame = False
    cur = conn.cursor()
    cur.execute(f"""Select * from books WHERE title LIKE "%{self.title}%" AND authorID = {self.authorID};""")
    rows = cur.fetchall()
    if (len(rows) > 0):
        isSame = True
    return isSame

