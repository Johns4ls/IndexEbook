def insert(self, conn):
    query = "insert into books (title, releaseDate, pages, authorID)"
    query += "values ('%s', %s, %s, %s);" % (self.title, self.releaseDate, self.pages, self.authorID)
    print(query)
    conn.execute(query)