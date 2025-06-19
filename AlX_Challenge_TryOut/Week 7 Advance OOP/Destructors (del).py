"""
Destructors (__del__):
When you create an object in Python, it occupies memory to store its data and code.
Objects are automatically destroyed (garbage collected) by Python when they are no longer in use or
when the program exits.

The __del__ Method:

The __del__ method is a special method in Python classes that gets called when an object is about to be
destroyed (garbage collected). You can define this method in your class to perform cleanup tasks or release
resources held by the object before it is destroyed.

"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("Good bye, see you later")


Lady1 = Person("Yvonne", 24)
print(Lady1.name)


"""
Let’s consider an example where we want to close a file automatically when the object representing that 
file is no longer needed.
"""

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r')  # Open the file for reading

    def read_data(self):
        return self.file.read()

    def __del__(self):
        self.file.close()  # Close the file when the object is destroyed

# Create an object of FileHandler
file_obj = FileHandler('sample.txt')
print(file_obj.read_data())

# Object is no longer needed, it will be garbage collected, and __del__ method will be called automatically to close the file
