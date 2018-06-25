file1 = open("D:\\test1.txt","r")
## "r" signifies that file is opened in read only mode
file1.read()
## Now let's try reading it again
file1.read()
# above command return empty string because our earlier read() function scaned file and moved cursor to end of file
# and hence getting blank result
# we can reset cursor poistion in file to read entire file again
file1.seek(0,0)
file1.read()
## seek unction helps us reset cursor position in row and column index.
file1.seek(1,0)
file1.read()
file1.seek(0,2)
file1.read()
file1.tell()
file1.seek(0,0)
file1.read(21)
file1.read(21)
