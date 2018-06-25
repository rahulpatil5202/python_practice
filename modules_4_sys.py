import sys

#lets use some of sys functions

print("Enter new line to test sys.stdin.readline function\n")
inStatement = sys.stdin.readline()
print(inStatement)

# we can set limit to number of characters to be read
print("Let's try limiting input to 10 characters only\n")
inStatement2 = sys.stdin.readline(10)
print(inStatement2)

print("now let's print something using stdout.write function of sys module\n")
sys.stdout.write("This is awesome!\n")
print("Let's check sys version using sys.version\n")
print(sys.version)
