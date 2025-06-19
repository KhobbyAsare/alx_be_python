"""
Static Attribute (Class Attribute)
A static attribute, also known as a class attribute, is an attribute that is bound to the class itself rather than to
any specific instance of the class. This means that all instances of the class share the same static attribute.
Static attributes are defined directly within the class and are not prefixed with self in the constructor or any
instance methods.

Key Points:
Shared Across Instances: Since static attributes are shared among all instances of a class, changes to a static
attribute will be reflected across all instances.
Access: Static attributes can be accessed both through the class itself and through any instance of the class.
However, it's generally recommended to access them through the class to avoid confusion.
Use Cases: Static attributes are useful for storing data that is common to all instances of a class, such as counts,
default values, or class-level settings.

Example:

"""

class User:
    user_count = 0  # Static attribute

    def __init__(self, username, email):
        self.username = username  # Instance attribute
        self.email = email  # Instance attribute
        User.user_count += 1  # Increment the static attribute

    def display_user(self):
        print(f"Username: {self.username}, Email Address: {self.email}")

# Creating instances of the User class
user1 = User('Enoch', "enoch@gmail.com")
user2 = User('Adams', "adams@gmail.com")

# Accessing the static attribute
print(User.user_count)  # Output: 2
print(user1.user_count)  # Output: 2
print(user2.user_count)  # Output: 2

"""
Instance Attribute
An instance attribute is an attribute that is unique to each instance of a class. These attributes are defined in 
the constructor method (__init__) and are prefixed with self. Each instance of the class has its own copy of these 
attributes, and changes to one instance's attributes do not affect other instances.

Key Points:
Unique to Each Instance: Instance attributes store data that is specific to each object created from the class.
Access: Instance attributes are accessed using the self keyword within the class methods and through the 
instance outside the class.
Use Cases: Instance attributes are ideal for storing data that varies from one instance to another, such as 
user-specific settings or object-specific data.

Example:
"""

class User:
    def __init__(self, username, email):
        self.username = username  # Instance attribute
        self.email = email  # Instance attribute

    def display_user(self):
        print(f"Username: {self.username}, Email Address: {self.email}")

# Creating instances of the User class
user1 = User('Enoch', "enoch@gmail.com")
user2 = User('Adams', "adams@gmail.com")

# Accessing instance attributes
user1.display_user()  # Output: Username: Enoch, Email Address: enoch@gmail.com
user2.display_user()  # Output: Username: Adams, Email Address: adams@gmail.com


"""
When to Use Each:

Static Attributes: Use static attributes for data that is common to all instances of a class. This includes counts, 
default values, and class-level settings. Static attributes are useful when you need to maintain information that is
shared across all instances.

Instance Attributes: Use instance attributes for data that is unique to each instance of a class. This includes 
object-specific data that varies from one instance to another. Instance attributes are ideal for storing information 
that is specific to each object created from the class.
"""


"""
Static Methods

A static method in python is a method that belongs to the class
itself rather than any instance of the class

# to define a static method, we use `@staticmethod` decorator
"""


# Static and Instance Methods
class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance =0):
        self.owner = owner
        self.__balance = balance #Encapsulation, preventing an attribute from being accessed and providing
        # a single and secured way of accessing anf updating that attribute

    #instance method
    def deposit(self, amount):  # single way of depositing to the balance attribute
        if self._is_valid_amount(amount):
            self.__balance += amount
            self.__log_transaction("deposit",amount)
        else:
            raise ValueError("Deposit amount must be positive")

    # protected method (Single Underscore)
    def _is_valid_amount(self,amount):
        return  amount > 0

    #private method (Double Underscore)
    def __log_transaction(self, transaction_type, amount):
        print(f"Logging the transaction type of ${amount}. New balance: ${self.__balance}")

    @staticmethod
    def is_valid_interest_rate(rate): # static method that sits on the class but not an instance method like the above one
        return 0 <= rate <= 5



account = BankAccount('Alice', 500)
account.deposit(200)

#accessing the static method
print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))


"""
static methods are ideal for tasks that are related to the classes domain and dont require
any specific instance data.

- we can use static methods for utility function that will help do something
- we can use it to help process a data or formate outputs that don't require any instance specific data

`@staticmethods` enforces encapsulation by keeping related functionality in the relevant class
"""



