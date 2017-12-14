import os
import zipfile 

dir = '__/__/'

# THE BELOW THINGS CAN BE CHANGED.
dir_dest = '__/__/UNZIPS/'
dir_src = '__/__/ZIPS/'

def dir_exist(dir):
    return os.path.isdir(dir)

def listing_items(dir):
    os.chdir(dir)
    return os.listdir(os.getcwd())

def file_extension_detect(file_name):
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

print dir_exist(dir)

if dir_exist(dir):
    items = []
    items +=  listing_items(dir_src)
    print items 
    os.chdir(dir_dest)

    for x in range(len(items)):   #.size()):
        if not (os.path.isdir(file_extension_detect(items[x]))):
            os.mkdir(file_extension_detect(items[x]))
        else:
            print ("Folder already exists")

    unzip_counter = []
    for x in range(len(items)):   #.size()):
        Y = items[x]
        unziped = directory_extend(dir_dest, file_extension_detect(items[x]))

        list = os.listdir(unziped) # dir is your directory path
        number_files = len(list)

        if (number_files != 0):
            print ("Already unzipped: " + Y + "\n")
        else:
            unzip(directory_extend(dir_src, Y), directory_extend(dir_dest, file_extension_detect(items[x]))) 
            unzip_counter += [Y]

    print ("You have unzipped: \n" + str(unzip_counter))
