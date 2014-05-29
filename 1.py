import sys
import os

allchars = {}
allwords = {}
result = open('result.txt', 'w')


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
    dirlist = []
    for file in file_list:
        dirlist.append(directory + file)
    return dirlist


def get_chars(file):
    result.write('Characters: \n')
    fd = open(file)
    data = fd.read()
    charlist = {}
    for char in data:
        if char not in charlist:
            charlist[char] = 1
        else:
            charlist[char] += 1
        if char not in allchars:
            allchars[char] = 1
        else:
            allchars[char] += 1
    for c, n in charlist.items():
        result.write(c + ': ' + str(n) + '\n')
    result.write('\n')


def get_words(file):
    result.write('Words: \n')
    fd = open(file)
    data = fd.read()
    data = data.replace('.', '').replace('-', ' ').replace(',', ' ')
    wordlist = {}
    for word in data.split():
        if word not in wordlist:
            wordlist[word] = 1
        else:
            wordlist[word] += 1
        if word not in allwords:
            allwords[word] = 1
        else:
            allwords[word] += 1
    for w, n in wordlist.items():
        result.write(w + ': ' + str(n) + '\n')
    result.write('\n')


direct = get_dir(sys.argv)
files = get_files(os.listdir)
directory = get_dirlist(files, direct)

for file in directory:
    result.write('File from directory: ' + file + '\n\n')
    get_chars(file)
    get_words(file)
    result.write('\n')

result.write('Characters from all files:\n')

for g, n in allchars.items():
    result.write(g + ': ' + str(n) + '\n')

result.write('\nWords:\n')

for g, n in allwords.items():
    result.write(g + ': ' + str(n) + '\n')
