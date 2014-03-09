import sys
import os

def get_dir(argv):
	defdir = "E:\\VU\Python\Files"
	if len(argv) > 1:
		return argv[1]
	else:
		return defdir
		
def get_files(listdir):
	dirs = os.listdir(direct)
	return dirs
	
direct = get_dir(sys.argv)
files = get_files(os.listdir)

