# constructor: A constructor is a special method in a class that is automatically called when an object of the class is created
# to intialize the object's attribiutes. In python, the constructor is defined using the '__init__' method. It allow you to set initial values for the objecct's attributes when you create an intance of the class.

class myConstructor():
    # the __init__ method is the constructor of the class. 
    # It is called when an object of the class is created.
    # It takes self as the first paramenter, which refers to the instance being created.
    def __init__(self, name, age):
        self.name =  name
        self.age = age

    def display(self):
        print(f'name: {self.name}\nage: {self.age}')

onj = myConstructor('Nupur', 24)
onj.display()    