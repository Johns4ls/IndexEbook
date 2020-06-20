#This function gets the last inserted ID of the author's table.
def getAuthorID(conn):

    #This is our SQL statement to get the last ID from the authors table.
    sql = "Select MAX(authorID) from authors;"

    #Lets get the cursor and then execute the SQL statement.
    conn = conn.cursor()
    conn.execute(sql)

    #We will return 1, which still returns a list so lets loop through and set the one equal to itself.
    result = conn.fetchone()
    for result in result:
        result = result

    #Lets return the ID back.
    return result

#This function gets the last inserted ID of the book's table.
def getBookID(conn):

    #This is our SQL statement to get the last ID from the books table.
    sql = "Select MAX(bookID) from books;"

    #Lets get the cursor and then execute the SQL statement.
    conn = conn.cursor()
    conn.execute(sql)

    #We will return 1, which still returns a list so lets loop through and set the one equal to itself.
    result = conn.fetchone()
    for result in result:
        result = result

    #Lets return the ID back.
    return result