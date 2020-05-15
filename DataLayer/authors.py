def insert(self, conn):
    query = "insert into authors (name)"
    query += "values ('%s');" % (self.name)
    conn.execute(query)