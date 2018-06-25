oldFileName = input("Enter filename to be copied\n")

file1 = open(oldFileName,"r")
file2 = open("D:\\copiedFile.txt", "w")
file2.write(file1.read())

file1.close()
file2.close()

file2 = open("D:\\copiedFile.txt", "r")
file2.read()
