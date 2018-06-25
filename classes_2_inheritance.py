class Parent:
        counter = 10
        def __init__(self):
                print("Parent class object being initialized")
        def parentFunc(self):
                print("ParentFunc being called")
        def setCounter(self, num):
                print("New value to counter being set")
                Parent.counter = num
        def showCounter(self):
                print(str(Parent.counter))

        
class Child(Parent):
        def __init__(self):
                print("Child class object being initialized")
        def childFunc(self):
                print("ChildFunc being called")

        
c = Child()
c.childFunc()
c.parentFunc()
print(str(c.counter))
c.setCounter(20)
c.showCounter()

