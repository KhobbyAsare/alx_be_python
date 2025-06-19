
# Single Inheritance

class Shape:
    def __init__(self, width, length, radius):
        self.radius = radius
        self.width = width
        self.length = length

    def calculate_area(self, shape_name:str):
        match shape_name:
            case "rectangle":
                return self.width * self.length
            case "square":
                return 3.14 * (self.radius * 2)



class Rectangle(Shape):
    def __init__(self, width, length, radius):
        super().__init__(width, length, radius)


class Square(Shape):
    def __init__(self, width, length, radius):
        super().__init__(width, length, radius)



rectangle1 = Rectangle(2,5, 4)
print(rectangle1.calculate_area("rectangle"))


square1 = Rectangle(3,6, 6)
print(square1.calculate_area("square"))


# Exercise 2: Multiple Inheritance Instruction:

class Bird:
    def fly(self):
        print("Bird is flying")


    def run(self):
        print("Bird is running")


class Mammal:
    def fly(self):
        print("Mammal is flying")


    def run(self):
        print("Mammal is running")



class Bat(Bird, Mammal):
    # Methods Overriding
    def fly(self):
        print("Bat is flying")


    def run(self):
        print("Bat is running")



bat1 = Bat()
bat1.run()
bat1.fly()

"""
Method Resolution Order (MRO)

Method Resolution Order (MRO) is the order in which Python searches for methods in classes during method calls, 
especially in cases of multiple inheritance (when a class inherits from more than one parent class). MRO helps Python 
determine which method to execute when there are method name conflicts or ambiguity due to inheritance.

How does Python determine MRO?

Python uses the C3 Linearization algorithm to calculate the Method Resolution Order. It follows a depth-first 
left-to-right search pattern to maintain the order of inheritance and resolve method conflicts effectively.
"""

class Dog(Bird, Mammal):
    pass

dog1 = Dog()
dog1.run()
dog1.fly()


# Exercise 3: Polymorphism with Duck Typing Instruction:


class Dog:
    def make_sound(self):
        print("woo")

class Cat:
    def make_sound(self):
        print("miaow")

class Bird:
    def make_sound(self):
        print("hew")



list_of_animals = [Dog(), Cat(), Bird()]

for animal in list_of_animals:
    animal.make_sound()

