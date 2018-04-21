#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#RM 03/22/2018 2022 create a basics.py non Python os, file programs.
#RM Python code containing os, file code

#2. Write a Python program to get the Python version you are using
import sys
print(sys.version) #print 3.5.2 (default, Nov 17 2016, 17:05:23)\n [GCC 5.4.0 20160609]
print(sys.maxsize) #print 9223372036854775807

#7. Write a Python program to accept a filename from the user and print the extension of that.  RM:  skipped accept a filename from the user
import os
filename, fileextension = os.path.splitext("/home/mar/Python/socratica/googlestockdata.csv")
print(filename) #print /home/mar/Python/socratica/googlestockdata
print(fileextension) #print .csv

#11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).  RM:  comment out print statements for #11
print(abs.__doc__)
print(print.__doc__)
print(type.__doc__)
print(dir(__builtins__)) #['ArithmeticError', 'AssertionError', ...,  'type', 'vars', 'zip']
RM:  https://docs.python.org/3/library/functions.html website has all built-in functions

#41. Write a Python program to check whether a file exists.
filename = "temptestmatplotlib.py"
with open(filename) as fileobject:
	reviewopenfile=fileobject.read()
print(reviewopenfile)
filename = "temptestmatplotlib2.py"
try:
	with open(filename) as fileobject:
		contents=fileobject.read()
except FileNotFoundError:
	print(filename+" file doesn't exist.")
else:
	print(contents)

#42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
import ctypes
print(ctypes.sizeof(ctypes.c_voidp)) #print 8.  4 for 32bit or 8 for 64bit
import platform
print(platform.architecture()) #print ('64bit', 'ELF')

#43. Write a Python program to get OS name, platform and release information.
import os
print(os.name) #print posix
import platform
print(platform.system()) #print Linux
print(platform.release()) #print 4.4.0-89-generic

#44. Write a Python program to locate Python site-packages.  site-packages is the location where Python installs its modules.
import sys
print([f for f in sys.path if f.endswith('packages')]) #print ['/home/mar/.local/lib/python3.5/site-packages', '/usr/local/lib/python3.5/dist-packages', '/usr/lib/python3/dist-packages']

#45. Write a python program to call an external command in Python.
#RM:  skip for now.

#46. Write a python program to get the path and name of the file that is currently executing.  RM:  also folder name or directory name. 
import os
print(os.path.basename(__file__)) #print pythonexercises.py
print(os.path.realpath(__file__)) #print /home/mar/Python/w3resource/pythonexercises.py
print(os.path.dirname(os.path.realpath(__file__))) #print /home/mar/Python/w3resource
foldername = os.path.realpath(__file__)
print(os.path.dirname(foldername)) #print /home/mar/Python/w3resource
import sys
print(sys.argv[0]) #print pythonexercises.py
print(sys.argv) #print ['pythonexercises.py']

#47. Write a Python program to find out the number of CPUs using.
import multiprocessing
print(multiprocessing.cpu_count()) #print 2

#49. Write a Python program to list all files in a directory in Python. 
import os
for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename) #prints all file names its extension

#51. Write a Python program to determine profiling of Python programs. Go to the editor  Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module.

#52. Write a Python program to print to stderr.

#53. Write a python program to access environment variables.
import os
print(os.environ)

#54. Write a Python program to get the current username
import getpass
username = getpass.getuser()
print(username)

#55. Write a Python to find local IP addresses using Python's stdlib

#56. Write a Python program to get height and width of the console window.
import os
ts = os.get_terminal_size()
print(ts.lines)
print(ts.columns)

#63. Write a Python program to get an absolute file path.
import os
print(os.path.abspath(__file__))

#64. Write a Python program to get file creation and modification date/times.
import os, time
print(os.stat(__file__))
print(os.path.getctime(__file__))
print(os.path.getmtime(__file__))
print(time.ctime(os.path.getctime(__file__))+" creation date")
print(time.ctime(os.path.getmtime(__file__))+" modified date")
print("Can't get creation date in Linux FYI.")

#70. Write a Python program to sort files by date.  RM:  used sample solution
import glob
import os
files = glob.glob("*.py")
files.sort(key=os.path.getmtime)
print("\n".join(files))
#RM:  First time I saw glob module

#71. Write a Python program to get a directory listing, sorted by creation date.  RM:  used sample solution
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time
#Relative or absolute path to the directory
dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'
#all entries in the directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)
#regular files, insert creation date
data = ((stat[ST_CTIME], path)
           for stat, path in data if S_ISREG(stat[ST_MODE]))
for cdate, path in sorted(data):
    print(time.ctime(cdate), os.path.basename(path))

#75. Write a Python program to get the copyright information.
#RM:  used sample solution. i.e. print the Python Copyrights
import sys
print("Python Copyright Information")
print(sys.copyright)

#76. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
#RM:  used sample solution.
import sys
print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))

#77. Write a Python program to test whether the system is a big-endian platform or little-endian platform.
#RM:  used sample solution.
import sys
if sys.byteorder == "little":
    #intel, alpha
    print("Little-endian platform.")
else:
    #motorola, sparc
    print("Big-endian platform.")

#79. Write a Python program to get the size of an object in bytes.
import sys
x = 2
print(sys.getsizeof(x)) #print 28
print(sys.getsizeof("this also")) #print 58

#80. Write a Python program to get the current value of the recursion limit.
#RM:  used sample solution.
import sys
print("Current value of the recursion limit:")
print(sys.getrecursionlimit())

#85. Write a Python program to check if a file path is a file or a directory.
#RM copied solution
import os  
path="abc.txt" #print It is a special file (socket, FIFO, device file)
#path = "pythonexercises.py" #print It is a normal file
#path = "/home/mar/Python/w3resource" #print It is a directory
if os.path.isdir(path):  
    print("\nIt is a directory")  
elif os.path.isfile(path):  
    print("\nIt is a normal file")  
else:  
    print("It is a special file (socket, FIFO, device file)" )
print()

#87. Write a Python program to get the size of a file (or file size filesize)
'''
1 Byte = 8 Bit
1 Kilobyte = 1,024 Bytes
1 Megabyte = 1,048,576 Bytes
1 Gigabyte = 1,073,741,824 Bytes
1 Terabyte = 1,099,511,627,776 Bytes
'''
import os
statinfo = os.stat("pythonexercises.py")
print(statinfo) #print os.stat_result(st_mode=33204, st_ino=524627, st_dev=2049, st_nlink=1, st_uid=1000, st_gid=1000, st_size=739, st_atime=1519783679, st_mtime=1519783678, st_ctime=1519783678)
print(statinfo.st_size) #print 739
print(statinfo.st_size/1048576,"mb")
print(statinfo.st_size/1073741824,"gb")
print(statinfo.st_size/1099511627776,"tb")

from pathlib import Path
file = Path() / 'pythonexercises.py'  # or Path('./doc.txt')
size = file.stat().st_size
print(size) #print 739

#94. Write a Python program to convert a byte string to a list of integers.
import sys
xstring = "abcdefghijklmnopqrstuvwyz"
bytestring = sys.getsizeof(xstring)
print(bytestring) #print 74
bytestring = str(bytestring)
listintegers = []
for eachbytestring in bytestring:
	listintegers.append(eachbytestring)
listintegers = list(map(int,listintegers))
print(listintegers) #print [7,4]

#bonus random generator string
from random import randint, choice
numberstrings = randint(1,101)
xstring = []
counter = 1
while counter < numberstrings:
	asciinumber = choice([randint(65,90),randint(97,122)])
	xstring.append(chr(asciinumber))
	counter += 1
print("".join(map(str,xstring)))
bytestring = sys.getsizeof(xstring)
print(bytestring)
bytestring = str(bytestring)
listintegers = []
for eachbytestring in bytestring:
	listintegers.append(eachbytestring)
listintegers = list(map(int,listintegers))
print(listintegers)

#96. Write a Python program to print the current call stack.
#source: https://stackoverflow.com/questions/1156023/print-current-call-stack-from-a-method-in-python-code
import traceback
def f():
    g()
def g():
    for line in traceback.format_stack():
        print(line.strip())
f()
#solution
import traceback
def f1():return abc()
def abc():traceback.print_stack()
f1()
#RM:  what's current call stack?

#97. Write a Python program to list the special variables used within the language.  
#Python comes with a number of special variables and methods whose name is preceeded and followed by __.
#RM:  copied solution
s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
print( '\n'.join(' '.join(s_var_names[i:i+8]) for i in range(0, len(s_var_names), 8)) )

#99. Write a Python program to clear the screen or terminal.
import os
#os.system('cls')  # For Windows
os.system('clear')  # For Linux/OS X

#100. Write a Python program to get the name of the host on which the routine is running.
import socket
print(socket.gethostname()) #print mar-VirtualBox
import os
myhost = os.uname()[1]
print(myhost) #print mar-VirtualBox

#101. Write a Python program to access and print a URL's content to the console.
import urllib.request
contents = urllib.request.urlopen("http://www.google.com").read()
print(contents)
print("\n")

#solution
from http.client import HTTPConnection
conn = HTTPConnection("www.google.com")
conn.request("GET", "/")  
result = conn.getresponse()
# retrieves the entire contents.  
contents = result.read() 
print(contents)

#102. Write a Python program to get system command output.
#RM:  copied solution
import subprocess
# file and directory listing
returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
print("dir command to list file and directory")
print(returned_text)
#RM:  printed all the files in present directory

#103. Write a Python program to extract the filename from a given path.
#solution
import os
print(os.path.basename("/home/mar/Python/w3resource/basics.py")) #print basics.py

#better because it prints all files in a list from present directory
from os import walk
filenameslist = []
for (dirpath, dirnames, filenames) in walk("/home/mar/Python/w3resource"):
    filenameslist.extend(filenames)   
    break
print(filenameslist)

#104. Write a Python program to get the effective group id, effective user id, real group id, a list of supplemental group ids associated with the current process. Note: Availability: Unix.

#105. Write a Python program to get the users environment.
import os
print(os.environ)
print("\n")
#exampls of specific environment attributes
print(os.environ["HOME"]) #must be caps HOME
print(os.environ["LANGUAGE"]) #must be caps LANGUAGE

#106. Write a Python program to divide a path on the extension separator.  RM:  I don't understand.  w3 solution below.
import os.path
for path in [ 'test.txt', 'filename', '/user/system/test.txt', '/', '' ]:
    print('"%s" :' % path, os.path.splitext(path))

#107. Write a Python program to retrieve file properties.  List of files.  Files list.  File attributes.
import os
print(os.listdir()) #prints all files in present directory running Python file in a list format
for filename in os.listdir():
	info = os.stat(filename)
	print(filename,info)
	print(filename,"modification time",info.st_mtime)
print("\n")

import os.path
import time
#print present file to run Python
# print('File         :', __file__)
# print('Access time  :', time.ctime(os.path.getatime(__file__)))
# print('Modified time:', time.ctime(os.path.getmtime(__file__)))
# print('Change time  :', time.ctime(os.path.getctime(__file__)))
# print('Size         :', os.path.getsize(__file__))
#print all files in present directory running Python file
for filename2 in os.listdir():
	print('File         :', filename2)
	print('Access time  :', time.ctime(os.path.getatime(filename2)))
	print('Modified time:', time.ctime(os.path.getmtime(filename2)))
	print('Change time  :', time.ctime(os.path.getctime(filename2)))
	print('Size         :', os.path.getsize(filename2))
	print("\n")

#108. Write a Python program to find path refers to a file or directory when you encounter a path name.  RM:  copied solution
import os.path
for file in [ __file__, os.path.dirname(__file__), '/', './broken_link']:
    print('File        :', file)
    print('Absolute    :', os.path.isabs(file))
    print('Is File?    :', os.path.isfile(file))
    print('Is Dir?     :', os.path.isdir(file))
    print('Is Link?    :', os.path.islink(file))
    print('Exists?     :', os.path.exists(file))
    print('Link Exists?:', os.path.lexists(file))

#111. Write a Python program to make file lists from current directory using a wildcard.
import glob
file_list = glob.glob('*.*')
print(file_list)
file_list = glob.glob('*pl*')
print(file_list) #print ['salesreplistfour.txt', 'temptestmatplotlib.py']

#117. Write a Python program to prove that two string variables of same value point same memory location.  RM:  copied solution.
str1 = "Python"
str2 = "Python"
print("Memory location of str1 =", hex(id(str1)))
print("Memory location of str2 =", hex(id(str2)))

#136. Write a Python program to find files and skip directories of a given directory.
#RM:  Official solution
import os
print([f for f in os.listdir('/home/students') if os.path.isfile(os.path.join('/home/students', f))])

#139. Write a Python program to valid a IP address. 
#RM:  Official solution
import socket
addr = '127.0.0.2561'
try:
    socket.inet_aton(addr)
    print("Valid IP")
except socket.error:
    print("Invalid IP")

#142. Write a Python program to find the operating system name, platform and platform release date
import os
print(os.name) #print posix
import platform
print(platform.system()) #print Linux
print(platform.release()) #print 4.4.0-89-generic

#143. Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system.
import platform
print(platform.architecture()) #print ('64bit', 'ELF')

#145. Write a Python program to find the operating system name, platform and platform release date
import os
print(os.name) #print posix
import platform
print(platform.system()) #print Linux
print(platform.release()) #print 4.4.0-89-generic

#146. Write a Python program to find the location of Python module sources.
#RM:  Official solution
import sys
print("\nList of directories in sys module:")
print(sys.path)
print("\nList of directories in os module:")
import os
print(os.path)