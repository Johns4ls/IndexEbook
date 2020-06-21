#This is our module/folder Database
from app.Index import dataLoader
from app.Index.ISBNData import GoogleISBNData
from app.Index.EbookData import EbookQuery, MobiQuery, PDFQuery
from app.Database import database, tables
from app.Index.Log import Tee
from multiprocessing import Pool

# List files in the queue in the log
def list_targets(media_path, file_types):
	queue_Count = 0
	queue_list = ''
	check_path = os.path.exists(media_path)
	if not check_path:
		print "Path not found: " + media_path
		print "Ensure your media_path exists and is accessible."
		print "Aborting index."
	else:
		for root, dirs, targets in os.walk(media_path):
			for target_name in targets:
				if target_name.endswith(file_types):
					queue_Count += 1
					fullpath = os.path.normpath(os.path.join(str(root), str(target_name)))
					queue_list = queue_list + "\n" + (str(queue_Count) + ': ' + fullpath)
		if queue_Count == 1:
			print ("There is " + str(queue_Count) + " file in the queue:")
		elif queue_Count > 1:
			print ("There are " + str(queue_Count) + " files in the queue:")
		else:
			print ("There are no files to be indexed in " + media_path + ".")
		print queue_list
        return queue_Count, queue_list

def divideList(seq):
    return (seq[i::6] for i in range(6))

def indexBooks(queue_lists):
        try:
        print("Spinning up processes")
        with Pool(6) as p:
        p.map(processBooks, queue_lists)
    except:
        print("Index Failed!")

def processBooks(queue_list):
    conn = database.create_connection()
    for eBook in queue_list:
        if(eBook.endswith('.epub')):
            dataLoader.LoadData(conn, GoogleISBNData.query(EbookQuery.readEpub())[0])
        elif(eBook.endswith('.mobi')):
            dataLoader.LoadData(conn, GoogleISBNData.query(MobiQuery.readMobi())[0])
        elif(eBook.endswith('.pdf')):
            dataLoader.LoadData(conn, GoogleISBNData.query(PDFQuery.readPDF())[0])   

def index():
    print("Starting index at " + datetime.datetime.now().strftime('%H:%M:%S'))

    #Instantiate the files we can currently pull metadata from
    file_types = '.epub', '.mobi', '.pdf'
    #Collect the path of the file we are currently in
    Base_Path = os.path.dirname(os.path.abspath(__file__))
    #Path to eBook files
    media_path = "B:/Ebooks and Audiobooks/Ebooks"
    #Path to Log
    log_path = Base_Path + "/Log/Index.log"

    #Set up our log logic
    ftarg = open(log_path, 'w')
    original = sys.stdout
    sys.stdout = Tee(sys.stdout, ftarg)

    queue_count, queue_list = list_targets(media_path, file_types)

    queue_lists = divideList(queue_list)

    indexBooks(queue_lists)
    print("Completed index")