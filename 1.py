import sys
import os

def get_dir(argv):
	defdir = "E:\\VU\Python\Files\\"
	if len(argv) > 1:
		return argv[1]
	else:
		return defdir
		
def get_files(listdir):
	dirs = os.listdir(direct)
	return dirs
	
def get_dirlist(file_list, directory):
	dirlist=[]
	for file in file_list:
		dirlist.append(directory + file)
	return dirlist
	
direct = get_dir(sys.argv)
files = get_files(os.listdir)
directory = get_dirlist(files, direct)
fd = open(directory[0])
print (fd.read())

