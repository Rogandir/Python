import sys
import os

allchars={}
allwords={}

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
		if char not in allchars:
			allchars[char] = 1
		else:
			allchars[char] += 1
	
def get_words(file):
	fd = open (file)
	data = fd.read();
	data = data.replace('.', '').replace('-', ' ').replace(',', ' ')
	wordlist={}
	for word in data.split():
		if word not in wordlist:
			wordlist[word] = 1
		else:
			wordlist[word] += 1
		if word not in allwords:
			allwords[word] = 1
		else:
			allwords[word] += 1
			
	#for w,n in wordlist.items():
	#	print (w, n)	
	
direct = get_dir(sys.argv)
files = get_files(os.listdir)
directory = get_dirlist(files, direct)
for file in directory:
	get_chars(file)
	get_words(file)
	
for w,n in allwords.items():
	print (w, n)	
