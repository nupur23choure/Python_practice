# data abstraction in python is a way to hide the complex implementation details and show only the essential features of the object.
# This is typically done using abstract base classes (ABCs) and abstract methods.

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
    # here pass is used as a placeholder for the abstract method.

    #  why we use abstract base classes? 
    # Abstract base classes allow us to define a common interface for a group of related classes.
    # They can also enforce that certain methods must be implemented by any subclass, ensuring a coonsistent API.
    # Abstract methods are methods that are declared but contain no implementation.
    # here def make_sound(self) means?
    # It means that any subclass of Animal must provide an implementation for the make_sound method.
    #

# class Dog(Animal):
#     # def make_sound(self):
#         print("Woof!")

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow!")

# # Usage
# dog = Dog()
# dog.make_sound()  # Output: Woof!

# cat = Cat()
# cat.make_sound()  # Output: Meow!

# please give me one simple question this abstract class so i can practice.
# Question: Create an abstract class called Vehicle with an abstract method called start_engine.
# Then, Create two subclasses, Car and Motorcycle, that implement the start_engine method.

from abc import ABC, abstractmethod

class MyVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    # don't we need constructor here?
    # No need for consttructor in abstract class if we don't have any attributes to initialize. but if we have attributes, we can define a constructor in the abstract class.
    # if we are not create the contructor then why use self here?please ellaborate.
    # The self parameter is used to refer to the instance of the class. Even in an abstract class, methods need to be defined with self to access instance attributes or methods.
    # here please explain abstract class and abstract method, and how to recognize them?


class car(MyVehicle):
    def start_engine(self):
        print("Car engine started!")

class Mototrcycle(MyVehicle):
    def start_engine(self):
        print("Motorcycle engine started!")

# obj = MyVehicle() #This will raise an error because Myvehicle is an abstract class and cannot be instantiated directly.
car = car()
car.start_engine()

motor = Mototrcycle()
motor.start_engine()