from app import app
from app.Objects.authors import Author
from app.Database import database
from flask import request, jsonify
@app.route('/api/authors/get/all', methods=['GET'])
def getAllAuthors():
    #Get database connection
    conn = database.create_connection()

    #Attempt to find all authors for the user
    results = Author.findAll(conn)

    #Jsonify and return the results
    return jsonify(results)


@app.route('/api/author/get', methods=['GET'])
def getAuthor():
    #Get database connection
    conn = database.create_connection()
 
    # Check if a authorID was provided as part of the URL.
    if 'authorID' in request.args:
        # If a authorID is provided, assign it to a variable.
        try:
            authorID = int(request.args['authorID'])
        except:
            # If we cannot parse the ID, display an error in the browser.
            return "Error: Could not parse the authorID.", 500
    elif 'name' in request.args:
        name = None
        #if a name is provided, assign it to a variable.
        try:
            name = request.args['name']
        except:
            #if we cannot get a name, display an error
            return "Error: Could not parse the name", 500
        Author.search(conn, name)
    elif 'search' in rquest.args:
        search = None
        #if a search is provided, assign it to a variable 
        try:
            search = request.args['search']
        except:
            #if we cannot get the search, display an error
            return "Error: Could not parse the search", 500
        Author.search(conn, search)
    else:
        # If no authorID is provided, display an error in the browser.
        return "Error: No authorID field provided. Please specify a authorID.", 500

    #Attempt to find a author with that ID
    results = Author.findFromKey(conn, authorID)

    #Jsonify the results and send it back.
    return jsonify(results)

@app.route('/api/author/update', methods=['GET'])
def updateAuthor():
    #TODO

@app.route('/api/author/delete', methods=['GET'])
def deleteAuthor():
    #Get database connection
    conn = database.create_connection()
    authorID = None
    # Check if a authorID was provided as part of the URL.
    if 'authorID' in request.args:
        # If a authorID is provided, assign it to a variable.
        try:
            authorID = int(request.args['authorID'])
        except:
            # If we cannot parse the ID, display an error in the browser.
            return "Error: Could not parse the authorID.", 500
        Author.deleteFromKey(conn, authorID)
    else:
        # If no authorID is provided, display an error in the browser.
        return "Error: No authorID field provided. Please specify a authorID.", 500