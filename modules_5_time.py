import time

print("time.time() prints seconds passed from 1st Jan 1970")
print(time.time())

print("\n\ntime.time can be used to check time taken to executite some code")

def printNumbers(max):
    time1 = time.time()
    for i in range(0,max):
        print(i)
    time2 = time.time()
    print("\n\nTime taken to execute this code is " + str(time2-time1))

num = int(input("Enter number to enter for loop from 0 till entered number\n"))
printNumbers(num)

print("\n\n\nlet's check time.asctime function")
print(time.asctime())

print("\n\n\nLet's also check time.localtime function")
print(time.localtime())

print("\n\n\ntime.localtime returns named tuple which can be accessed using indices")
a=time.localtime()

print("first element year - " + str(a[0]))
print("Second element month - " + str(a[1]))
print("Third element day - " + str(a[2]))
print("and likewise...")

print("\n\n\nNow let's use time.sleep() to delay printing function")

for i in range(0,5):
    print(i)
    time.sleep(1)
