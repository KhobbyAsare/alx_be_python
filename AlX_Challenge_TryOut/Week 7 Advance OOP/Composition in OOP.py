# Example 1

class Car:
  def __init__(self, engine):
    self.engine = engine  # Engine object as an attribute

  def start(self):
    self.engine.start()

class Engine:
  def start(self):
    print("Engine starting...")


car = Car(Engine())
car.start()  # Output: Engine starting...

# Example 2

class Animal:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed

  def make_sound(self, sound):
    if sound:
        print(f"{self.name} says {sound}")
    else:
        print("Generic animal sound")

  # Dunder Methods............
  def __str__(self):
    return f"Name: {self.name}, Age: {self.breed}"

  def __repr__(self):
    return f"Name: {self.name}, Age: {self.breed}; Representation"




class Dog:
  def __init__(self, animal):
    self.animal = animal

  def make_sound(self, sound):
    self.animal.make_sound(sound)

dog = Dog(Animal('max', "Swis"))
dog.make_sound("Woof")  # Output: Woof!

"""
Magic Methods
Magic methods are special methods in Python that start and end with double underscores (also known as dunder methods). 
They allow you to define specific behaviors for your objects in various contexts, such as arithmetic operations, 
comparisons, string representations, and more. Here are some common examples:

__str__: Defines how an object is represented as a string.
__repr__: Defines the official string representation of an object.
"""


# Dunder Method
animal1 = Animal('max', "Swis")
print(animal1)
print(repr(animal1))

