#This function gets the last inserted ID of the author's table.
def getAuthorID(conn):
    sql = "Select MAX(authorID) from authors;"
    conn = conn.cursor()
    conn.execute(sql)
    result = conn.fetchone()
    for result in result:
        result = result
    return result

#This function gets the last inserted ID of the book's table.
def getBookID(conn):
    sql = "Select MAX(bookID) from books;"
    conn = conn.cursor()
    conn.execute(sql)
    result = conn.fetchone()
    for result in result:
        result = result
    return result