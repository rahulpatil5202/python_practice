f = open("D:\\test1.txt","a") # a signifies that file is opened for appending

f.write("This line is being appended to exsting content")
f.write("\nthis will be added to new line")
f.close()

f = open("D:\\test1.txt","r")
f.seek(0,0)
f.read()