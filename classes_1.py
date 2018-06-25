class Students: #creating new class
 def __init__(self, name, age, grade): #defining class initialization and adding variables
     self.name = name
     self.age = age
     self.grade = grade

     
student1 = Students("Rahul", 15, "2nd") #creating new object of class Students and initializing
print(student1.age)

print(hasattr(student1, "age")) #hasatttr return boolean value if attribute exists or not
print(getattr(student1, "name")) #getattr return attribute value for given object
setattr(student1, "name", "Aarav") #setattr sets new value to attribute
print(getattr(student1,"name"))
delattr(student1, "grade") # delattr deleter attribute from class object
print(getattr(student1,"grade"))

