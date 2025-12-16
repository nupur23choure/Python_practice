# what is deconstructor?
# A deconstructor (commonly called a destructor) is a special method in object-oriented programming
# that is called when an object is about to be destroyed. In Python, the destructor method is __del__().
# It is used to perform cleanup actions, such as releasing resources or closing files, when an object is deleted. 

class MyDestructor:
    def __init__(self, name):
        self.name = name
        print(f"object {self.name} created. ")

    def __del__(self):
        print(f"object {self.name} is being destroyed.")
        # perform cleanup action here, like closing files or releasing resources
    
    def deleted(self):      
        print(self.name, "is deleted.")


obj = MyDestructor("Nupur")
