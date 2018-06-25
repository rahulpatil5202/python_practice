class Parent:
        def func(self):
                print("This is parent function")


class Child(Parent):
        def func(self):
                print("This is child function")


c = Child()
c.func() #if child inherits same function name from parent then function from parent will be overrided by child

