import turtle

t = turtle.Pen()

t.forward(100)
t.left(90)

t.forward(100)
t.left(90)


t.forward(100)
t.left(90)


t.forward(100)
t.left(90)

#Similarly we can draw an octagone 
t.reset()
t = turtle.Pen()
for i in range(0,8):
    t.forward(100)
    t.left(360/8) #diving 360 by 8 as it is an octagone

t.reset()
##for i in range (0,38):
##    t.forward(100)
##    t.left(175)


t.reset()
for i in range (0,20):
    t.forward(100)
    t.left(95)

print("Using t.up() to lift pen pointer and move it to 100 pixels right")
t.up()
t.right(180)
t.forward(100)

print("check pointer position now")

t.down()
for i in range (0,20):
    t.forward(100)
    t.left(95)

t.reset()

print("Try drawing squares and circles using functions")

def drawSquare(side):
    for i in (0,4):
        t.forward(side)
        t.left(90)

drawSquare(10)
drawSquare(20)
drawSquare(30)
drawSquare(40)
drawSquare(50)

t.reset()

def drawCircle(radius):
    t.circle(radius)

drawCircle(10)
drawCircle(20)
drawCircle(30)
drawCircle(40)
drawCircle(50)
