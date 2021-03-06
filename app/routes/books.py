from app import app
from app.Objects.books import Book
from app.Database import database
from flask import request, jsonify, send_from_directory
@app.route('/api/books/get/all', methods=['GET'])
def getAllBooks():
    #Get database connection
    conn = database.create_connection()
 
    #Attempt to find all books for the user
    results = Book.findAll(conn)

    #Jsonify and return the results
    return jsonify(results)


@app.route('/api/book/get', methods=['GET'])
def getBook():
    #Get database connection
    conn = database.create_connection()

    # Check if a bookID was provided as part of the URL.
    if 'bookID' in request.args:
        bookID = None
        # If a bookID is provided, assign it to a variable.
        try:
            bookID = int(request.args['bookID'])
        except:
            # If we cannot parse the ID, display an error in the browser.
            return "Error: Could not parse the bookID.", 500
        #Attempt to find a book with that ID
        results = Book.findFromKey(conn, bookID)
        #Jsonify the results and send it back.
        return jsonify(results)
    elif 'title':
        title = None
        # Check if a name was provided as part of the URL.
        if 'title' in request.args:
            # If a name is provided, assign it to a variable.
            try:
                if(request.args['title'] is not None and request.args['title'] != ""):
                    title = request.args['title']
            except:
                # The input was invalid
                return "Error: Could not collect the title from the request", 500
        #Attempt to find a book with that title
        results = Book.searchTitle(conn, title)
        return jsonify(results)
    else:
        # If no bookID is provided, display an error in the browser.
        return "Error: No bookID field provided. Please specify a bookID.", 500

@app.route('/api/book/update', methods=['GET'])
def updateBook():
    #TODO
    Print("Unimplemented")

@app.route('/api/book/delete', methods=['GET'])
def deleteBook():
    #Get database connection
    conn = database.create_connection()
    bookID = None
    # Check if a bookID was provided as part of the URL.
    if 'bookID' in request.args:
        # If a bookID is provided, assign it to a variable.
        try:
            bookID = int(request.args['bookID'])
        except:
            # If we cannot parse the ID, display an error in the browser.
            return "Error: Could not parse the bookID.", 500
        Author.deleteFromKey(conn, bookID)
    else:
        # If no bookID is provided, display an error in the browser.
        return "Error: No bookID field provided. Please specify a bookID.", 500

@app.route("/api/book/download")
def get_file(path):
    if 'path' and 'fileName' in request.args:
        path = None
        fileName = None
        try:
            path = request.args['path']
        except:
            # If we cannot parse the ID, display an error in the browser.
            return "Error: Could not parse the path.", 500
        try:
            fileName = request.args['fileName']
        except:
            # If we cannot parse the ID, display an error in the browser.
            return "Error: Could not parse the fileName.", 500
        if(path is not None and fileName is not None):
            return send_from_directory(path, fileName, as_attachment=True)