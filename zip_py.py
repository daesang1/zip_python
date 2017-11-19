import os
import zipfile 

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
    return original + '/' + add

########################

dir = '_folder_location'

# print dir_exist(dir)

if dir_exist(dir):
    items = []
    source = dir + '/ZIPS'
    items +=  listing_items(source)
    print items 

    print os.getcwd()
    os.chdir('..')
    print os.getcwd()
    os.chdir('UNZIPS')

    for x in range(len(items)):   #.size()):
        if not (os.path.isdir(file_extension_detect(items[x]))):
            os.mkdir(file_extension_detect(items[x]))

    print (directory_extend(dir, 'UNZIPS'))   

     #   source = 'ZIPS', items[x]
     #   print source
     #   dest = 'UNZIPS', file_extension_detect(items[x])
     #   unzip(items[x], file_extension_detect(items[x]))
    
    os.chdir('..')    
    print os.listdir(os.getcwd()) 
    
    UN = directory_extend(dir, 'UNZIPS')
    ZI = directory_extend(dir, 'ZIPS')

    for x in range(len(items)):   #.size()):
        Y = items[x]
        unzip(directory_extend(ZI, Y), directory_extend(UN, file_extension_detect(items[x]))) 
       
     
    #for x in range(len(items)):   #.size()):
    #    os.chdir(file_extension_detect(items[x]))
    #    if not (os.path.isdir(file_extension_detect(items[x]))):
    #    os.mkdir(file_extension_detect(items[x]))
    #unzip()    

    
      

    #directory = "cd ", dir 
    #print (os.getcwd())
    #print (os.listdir(os.getcwd()))
           

