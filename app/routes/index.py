from app import app
from flask import request, jsonify
from app.Index import index
@app.route('/api/index', methods=['GET'])
def indexBooks():
    index.index()
    return "Success"