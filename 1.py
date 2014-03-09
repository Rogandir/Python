import sys

def get_dir(argv):
	defdir = "../Files"
	if len(argv) > 1:
		return 'exist'
	else:
		return 'wth dude?'
	
print(get_dir(sys.argv))
