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
	
def get_chars(file):
	fd = open (file)
	data = fd.read()
	charlist={}
	for char in data:
		if char not in charlist:
			charlist[char] = 1
		else:
			charlist[char] += 1
	#for c,n in charlist.items():
	#	print (c, n)
	return file
	
def get_words(file):
	fd = open (file)
	wordlist={}
	for word in fd.read().split():
		if word not in wordlist:
			wordlist[word] = 1
		else:
			wordlist[word] += 1
			
	#for w,n in wordlist.items():
	#	print (w, n)	
	
direct = get_dir(sys.argv)
files = get_files(os.listdir)
directory = get_dirlist(files, direct)
for file in directory:
	get_chars(file)
	get_words(file)


