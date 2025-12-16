# class - A class in Python is a blueprint for creating objects. It defines attributes (data) and methods (functions) that the created objects (instances) will have.
# object - An instance is a specific object created from a class. Each instance has its own unique data, but shares the structure and behavior defined by the class.
# self- self is a refernce of the currenct instance of the class. It is used to access variables that belong to the class.
#__init__ - the __init__ method is a special method in python classes. It is called a constructor and is used to initialize the attributes of the class when an object is created.
# The line self.a = num1 assigns the value of the parameter num1 to the instance variable a of the class.
# Explanation:
# self refers to the current object (instance) being created.
# a is an attribute (variable) that belongs to this object.
# num1 is a value passed to the constructor (__init__) when you create an object.
# The line self.a = num1 sets the instance variable a of the object to the value provided as the num1 argument during object creation.

# naming convention for the class is pascal case eg.(MYclassArithmetic).

# if __name__ == "__main__": - This line checks if the script is being run directly (not imported as a module). If it is, the code block under it will execute. This is often use to run test code or examples when the script is executed directly.


class arithmeticOpration():
    def __init__(self, num1, num2):
       self.a = num1
       self.b = num2

    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
    def mod(self):
        return self.a % self.b
       
obj1 = arithmeticOpration(10,5)
print("Addition: ", obj1.add())
print("Subtraction: ", obj1.sub())
print("Multiplication: ", obj1.mul())
print("Division: ", obj1.div())
print("Modulus: ", obj1.mod())

if __name__ == "__main__":
    print("This is a class object example.")

# 2. create a class of car with attributes like brand, model. and also create instance of the class.
class car():
    def __init__(self, brand, name):
        self.brand =  brand
        self.name = name
    def display(self):
        print(self.brand, self.name)

obj1 = car('Toyota', 'Carmy')
obj1.display()
