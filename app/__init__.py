from flask import Flask
__name__ = '__main__'
app = Flask(__name__)
app.config["DEBUG"] = True
from app.Objects import books, authors
from app.routes import books, authors, index