from PyPDF2 import PdfFileReader
import os

def readPDF(eBook):
    with open(eBook, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
    return  info.title + " " + info.author