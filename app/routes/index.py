from app import app
from flask import request, jsonify
from app.Index import index
@app.route('/api/index', methods=['GET'])
def indexBooks():
    try:
        index.index()
    except:
        return "Index failed"
    return "Index succeeded"