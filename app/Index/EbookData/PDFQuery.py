from PyPDF2 import PdfFileReader
import os

def readPDF():
    with open(os.path.dirname(os.path.abspath(__file__)) + '/book.pdf', 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
    
    print(info)
    return  info.title + " " + info.author