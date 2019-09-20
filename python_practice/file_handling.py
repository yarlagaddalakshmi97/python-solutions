'''
file handling

fh=open(<filename>,mode)
---by default mode will be read mode(r)
---
fh.close()--explicitly closing

with open(filename,mode) as fh     this by deafult closes the file
----
----
---
fh.read()--whole list
fh.readline()
fh.readlines()
fh.read(100)----will read only first 100 bytes
fh.writelines(list)

modes of file
read
write--delete the existing and writes
append--write continuing the existing file
rb-read binary--gives bytes of content--need to convert with utf8 to work
wb-write binary
ab-append binary

other methods
seek()--move the file pointer to wherever you want row and column
tell()--tells where the pointer is
flush()--clears the buffer

CSV,JSON file formats
'''
from os import read

fh=open('sample','w')
print ("File Name: ", fh.name)
print ("File Name: ", fh.mode)
print ("File Name: ", fh.closed)
print ("File Name: ", fh.softspace)


