# file input/output in python
#  python can be used to perform operation on a file 
#(read and write data)
#types of all files : 
# 1.text files: .txt, .docx ,.log (data store in character form)
# 2.Binary Files: .mp4,.mov, .png ,.jpeg
# both are store in 0 1 form i.e. binary form
# f= open("file_name","mode(r or w)") default is read
# open() opens the file , read() reds the whole file , readline() reads the single line
# close() closes the file 
# if the file is not in same folder thne we need to give the path of file
f=open("demo.txt","r")

line1= f.readline()
print(line1)

data =f.read()
print(data)
print(type(data))

data =f.read(4)
print(data)

f.close()

# r - open and read the file
# w - open and write in file (overwrite) truncating the file first (deletes the old data if present)
# x - creates a new file and open it for writing 
# a - open for writing , appending to the end (keeps the old data)
# b - binary mode
# t - text mode (default)
# + - open a disk file for uploding (reading and writhing)
# r+ - append at start and also can read the file
# w+ - delet the existing data then we can write and read also
# a+ - append at end and also can read the file
## open("file_name","mode") as f ; f is a variable assigned to file which can be used to perform various methods on file

f=open("demo.txt","w")
f.write("All going welll")
f.close()

f = open("demo.txt","r")
data = f.read()
print(data)
print(f.read())
f.close()

f=open("demo.txt","a")
f.write("where are you")
f.close()

f = open("demo.txt","r")
data = f.read()
print(data)
print(f.read())
f.close()

# deleting a file : using the os madule 
#module (like a code library) is afile wrriten by another programer that generally has a function we can use.
import os
os.remove("demo.txt")