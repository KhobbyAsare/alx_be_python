


class Animal:
    def __init__(self, name, breed, attitude):
        self.name = name
        self.breed = breed
        self.attitude = attitude

    def speak(self):
        pass

# Creating InStance of a Class

DogAnimal = Animal("Max", "German Shepard", "Wild")
print(DogAnimal.name)


# INHERITANCE IN CLASS

class Lion(Animal):
    def __init__(self, name, breed, attitude):
        super().__init__(name, breed, attitude)  # Correctly initialize the parent class

    def speak(self):        #overriding parents method in child class
        return f"{self.name} the {self.breed} says: Roar!"

# Create an instance of Lion
lion_instance = Lion(name="Simba", breed="African Lion", attitude="Aggressive")

# Call the speak method on the instance
print(lion_instance.speak())


"""
Explanation
Initialization: The Lion class initializes the Animal class using super().__init__(name, breed, attitude). 
This ensures that the attributes name, breed, and attitude are properly set in the Animal class.

Method Overriding: The speak method in the Lion class overrides the speak method in the Animal class. 
It returns a string that includes the lion's name and breed.

Instance Creation: An instance of the Lion class is created with specific values for name, breed, and attitude.

Method Invocation: The speak method is called on the instance of the Lion class, which outputs the string defined 
in the speak method.
"""


# POLYMORPHISM

"""
Polymorphism is a fundamental concept in object-oriented programming that allows objects of different classes to
 be treated as objects of a common superclass. It enables one interface to be used for a general class of actions, 
 and the specific action is determined by the exact nature of the situation. In Python, polymorphism is typically 
 achieved through method overriding and duck typing.
"""

class Animal2:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

class Lion2(Animal2):
    def speak(self):
        return f"{self.name} the lion says: Roar!"

class Dog(Animal):
    def speak(self):
        return f"{self.name} the dog says: Woof!"

# Function that demonstrates polymorphism
def animal_sound(animal):
    print(animal.speak())

# Create instances of Lion and Dog
lion = Lion2("Simba")
dog = Dog("Buddy")

# Use polymorphism to call the speak method
animal_sound(lion)  # Output: Simba the lion says: Roar!
animal_sound(dog)   # Output: Buddy the dog says: Woof!


"""
Explanation
Base Class (Animal): The Animal class defines a method speak that is intended to be overridden by subclasses. 
It raises a NotImplementedError to enforce that subclasses must provide their own implementation.

Subclasses (Lion and Dog): Both Lion and Dog are subclasses of Animal. They override the speak method to provide 
specific implementations for how a lion or a dog would speak.

Polymorphic Function (animal_sound): The animal_sound function takes an Animal object and calls its speak method. 
This function doesn't need to know the specific type of animal it's dealing with; it just calls the method. 
This is the essence of polymorphism: the ability to use a general interface for a variety of specific forms.

Polymorphism in Action: When animal_sound is called with different types of animals (Lion and Dog), it invokes 
the appropriate speak method for each type of animal. This demonstrates polymorphic behavior, where the same 
function call results in different actions based on the object type.

This example illustrates how polymorphism allows for more flexible and reusable code, as the same function can
operate on objects of different classes, invoking the appropriate methods for each class.
"""