import os
import zipfile 
import time

timer = 4

# THE BELOW THINGS CAN BE CHANGED.
dir_dest = ''
dir_src = ''

def dir_exist(dir):
    return os.path.isdir(dir)

def listing_items(dir):
	os.chdir(dir)
	counter = []
	for file in os.listdir(dir):
		if os.path.isfile(file):
			counter += [file]
	
	return counter
	
def file_extension_detect(file_name):
	if (file_name.find(".") != -1):
		dot_index = file_name[::-1].index('.')
		dot_index += 1
		return (file_name[::-1][dot_index:])[::-1]    

def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        zf.extractall(dest_dir)

def makedir(source, dest):
    items = []
    items +=  listing_items(source)
    os.chdir(dest)
    for x in range(len(items)):   #.size()):
        if not (os.path.isdir(file_extension_detect(items[x]))):
            os.mkdir(file_extension_detect(items[x]))     

def directory_extend(original, add):
    #print original, '/', add
    if ((original[-1:]) == '/'):
        return original + add
    else: 
        return original + '/' + add

########################

if (dir_dest == "" or dir_src == ""):
	print ("dir == 0")
	while (timer != 0):
		print ("This program will exit in " + str(timer) + "\n")
		time.sleep(1)
		timer -= 1 
	#pass
	#dir = '__/__/'
	# THE BELOW THINGS CAN BE CHANGED.
	#dir_dest = '__/__/UNZIPS/'
	#dir_src = '__/__/ZIPS/'	
else:
	print dir_exist(dir_src)
	if dir_exist(dir_src):
		items = []
		items +=  listing_items(dir_src)
		#print items
		#for x in range(len(items)):   #.size()):
			#print [items[x]] 
			#print 
			
		os.chdir(dir_dest)
		no_folder = []
		
		for x in range(len(items)):   #.size()):
			#print [items[x]]
			#print os.path.isdir(file_extension_detect(items[x]))
			if os.path.isdir(file_extension_detect(items[x])) is not None:
				if not (os.path.isdir(file_extension_detect(items[x]))):
					#print ("Folder does not exist: " + str(items[x]) + "\n")
					no_folder += [items[x]]
					#print ("Folder already exists")

		print ("You have non_existing_folder : \n")
		for x in range(len(no_folder)):
			print(no_folder[x])
			print 
			
		print
		print ("They are total: " + str(len(no_folder)))
		
		time.sleep(100)