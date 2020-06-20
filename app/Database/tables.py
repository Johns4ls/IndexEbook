#Here is our function to update our tables. We passed in the connection to the DB to use.
def update_tables(conn):

    #Here is our SQL to create our table for authors if it doesn't exist
    sql_authors_table = """CREATE TABLE IF NOT EXISTS authors (
                            authorID integer PRIMARY KEY,
                            name text NOT NULL
                        );"""
                        
    #Here is our SQL to create our table for books if it doesn't exist, notice the foreign key to the authors.
    sql_books_table = """ CREATE TABLE IF NOT EXISTS books (
                                    bookID integer PRIMARY KEY,
                                    title text NOT NULL,
                                    releaseDate date,
                                    pages integer,
                                    authorID integer,
                                    FOREIGN KEY (authorID) REFERENCES authors (authorID)
                                ); """

    #Lets grab our cursor and execute these SQL statements against the database.
    conn.execute(sql_authors_table)
    conn.execute(sql_books_table)
        
