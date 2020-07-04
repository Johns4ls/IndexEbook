#This is our module/folder Database
from app.Index import dataLoader
from app.Index.ISBNData import GoogleISBNData
from app.Index.EbookData import EbookQuery, MobiQuery, PDFQuery
from app.Database import database, tables
from app.Index.Log.Log import Tee
from multiprocessing import Pool
from multiprocessing import cpu_count
from datetime import datetime
import os
import sys

# List files in the queue in the log
def list_targets(media_path, file_types):
	queue_Count = 0
	queue_list = []
	check_path = os.path.exists(media_path)
	if not check_path:
		print ("Path not found: " + media_path)
		print ("Ensure your media_path exists and is accessible.")
		print ("Aborting index.")
	else:
		print("Starting search")
		for root, dirs, targets in os.walk(media_path):
			for target_name in targets:
				if target_name.endswith(file_types):
					queue_Count += 1
					fullpath = os.path.normpath(os.path.join(str(root), str(target_name)))
					print(fullpath)
					queue_list.append(fullpath)
		if queue_Count == 1:
			print ("There is " + str(queue_Count) + " file in the queue:")
		elif queue_Count > 1:
			print ("There are " + str(queue_Count) + " files in the queue:")
		else:
			print ("There are no files to be indexed in " + media_path + ".")
		return (queue_Count, queue_list)

def divideList(lst):
    """ Yield n successive chunks from l.
    """
    print(int(len(lst)))
    print(cpu_count())
    newn = int(len(lst) / cpu_count())
    for i in range(0, cpu_count()):
        yield lst[i*newn:i*newn+newn]
    return lst[cpu_count()*newn-newn:]

def indexBooks(queue_lists):
    print("Spinning up processes")
    with Pool(processes=cpu_count()) as p:
        p.map(processBooks, queue_lists)

def processBooks(queue_list):
    print("processing books")
    conn = database.create_connection()
    for eBook in queue_list:
        if(eBook.endswith('.epub')):
            dataLoader.LoadData(conn, GoogleISBNData.query(EbookQuery.readEpub(eBook))[0])
        elif(eBook.endswith('.mobi')):
            dataLoader.LoadData(conn, GoogleISBNData.query(MobiQuery.readMobi(eBook))[0])
        elif(eBook.endswith('.pdf')):
            dataLoader.LoadData(conn, GoogleISBNData.query(PDFQuery.readPDF(eBook))[0])   

def index():
    print("Starting index at " + datetime.now().strftime('%H:%M:%S'))

    #Instantiate the files we can currently pull metadata from
    file_types = '.epub', '.mobi', '.pdf'
    #Collect the path of the file we are currently in
    Base_Path = os.path.dirname(os.path.abspath(__file__))
    #Path to eBook files
    media_path = "/mnt/external/Lovecraft"
    #Path to Log
    log_path = Base_Path + "/Log/Index.log"

    queue_count, queue_list = list_targets(media_path, file_types)
    queue_lists = divideList(queue_list)

    indexBooks(queue_lists)
    print("Completed index")