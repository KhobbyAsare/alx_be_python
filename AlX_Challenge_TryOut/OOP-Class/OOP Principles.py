# Encapsulation
"""
Encapsulation helps hide the internal implementation details of the class by only
exposing the necessary functionalities to the outside world.
"""

class BadBackAccount:
    def __init__(self, balance):
        self.balance = balance


# account = BadBackAccount(0.0)
# account.balance = -1
# print(account.balance)

class BetterBackAccount:
    def __init__(self):
        self.__balance:float = 0.0

    @property # getter property method
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise  ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        elif self.__balance <= amount:
            raise ValueError("Insufficient Balance")
        self.__balance -= amount


account1 = BetterBackAccount()
print(account1.balance)
account1.deposit(50)
print(account1.balance)
account1.withdraw(20)
print(account1.balance)

"""
the implementation details for the bank is hidden from the user and it has provided
a single point to deposit and withdrawal to the user to run some operation on their account

- they dont have to worry about the complex details of withdrawing and depositing from and into their account
- when they do something silly, like trying to pass in negatives or zero the program will throw an error for them to be 
notified

So in summary encapsulation allows for clear separation between the public interface and the internal implementation of
a class providing you with just a simplified and intuitive way to interact with objects while hiddent the complexity of 
those interactions are handled internally
"""


# Abstraction

"""
Reduce complexity by hiding unnecessary details
"""

class EmailService:

    def __connect(self):
        print("Connecting to email server")

    def __authentication(self):
        print("Authenticating..")

    def __disconnect(self):
        print("Disconnecting from email server..")

    def send_email(self):
        self.__connect()
        self.__authentication()
        print("Sending Email....")
        self.__disconnect()


"""
the user of this class must not know the internal details of how to send an email
they have been abstracted away from the users view

without abstraction the user will have more options and decision to make, that can lead them to be 
confused when they want to perform a task.
"""

email = EmailService()
email.send_email()

# if we are not using abstraction and the methods are public
# we will be compiled to do these manually, which is complex and repetition
#
# self.connect()
# self.authentication()
# print("Sending Email....")
# self.disconnect()

"""
Differences Between Encapsulation and Abstraction

- Encapsulation focuses on bundling data or attributes and methods
that operate on that data into a single unit called the class and it restrict access to the internal
implementation details, so this is achieved by defining attributes and methods as private and protected
and exposing only a controlled interface or public methods: eg: by marking connected, disconnect and authentication
as private or protected hides that details of the email service class

- Abstraction focuses on hiding complexity be providing a simplified, high level interface to interact with, so jest
by providing the send_email method, when called we are concealing the underline implementation by calling the private
methods to send an email. it allows you to focus on what an object does rather than how it does it.

"""

#Inheritance

"""
Inheritance is a fundamental concept in object-oriented programming (OOP)
that involves creating new classes (subclasses or derived classes) based
on existing class (Super class or base class). which they can add new features or
override existing ones.

- Inheritance is most define as is-a relationship
EG:
# A Car is-a Vehicle
# A Bike is-a Vehicle
"""

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f"Vehicle {self.brand} is starting...")

    def stop(self):
        print(f"Vehicle {self.brand} is stopping...")



class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        super().__init__(brand, model, year) # meaning we are calling the super class which is Vehicle
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels


class Bike(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels


car = Car("Ford","Focus",2008,5,4)
bike = Bike("Honda", "Scoopy", 2018,2 )

print(car.__dict__)
print(bike.__dict__)
print(car.start())
print(bike.start())


# Polymorphism

"""
the word polymorphism is derived from Greek and means 'having multiple forms'

Poly = many

Morph = forms

Polymorphism is the ability of an object to take many forms
"""


class PolyCar:
    def __init__(self, brand, model, year, number_of_doors):
        self.brand = brand
        self.model = model
        self.year = year
        self.number_of_doors = number_of_doors

    def start_car(self):
        print(f"Car {self.brand} is starting...")

    def stop_car(self):
        print(f"Car {self.brand} is stopping...")


class Motorcycle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_bike(self):
        print(f"Motorcycle {self.brand} is starting...")

    def stop_bike(self):
        print(f"Motorcycle {self.brand} is stopping...")


# create list of vehicle to inspect

vehicles = [
    PolyCar('ford','focus',2008,6),
    Motorcycle('Honda','Scoopy', 2018)
]

# loop through list of vehicle and inspect them
for vehicle in vehicles:
    if isinstance(vehicle, PolyCar):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start_car()
        vehicle.stop_car()
    elif isinstance(vehicle, Motorcycle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.stop_bike()
        vehicle.start_bike()
    else:
        raise Exception("Object is not a valid vehicle")

"""
Issue: the for loop will continue to grow and look ugly as more object is add, which will become difficult to handle

We can fix this with polymorphism
"""


class VehiclePoly:
    def __init__(self,brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print('Vehicle is starting..')

    def stop(self):
        print('Vehicle is stopping..')


class NewPloyCar(VehiclePoly):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors


    # Overriding the methods in the superclass
    def start(self):
        print(f"Car {self.brand} is starting...")

    def stop(self):
        print(f"Car {self.brand} is stopping...")

class NewPolyMotorcycle(VehiclePoly):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    # Overriding the methods in the superclass
    def start(self):
        print(f"Motorcycle {self.brand} is starting...")

    def stop(self):
        print(f"Motorcycle {self.brand} is stopping...")

print(" ")
print("...........Polymorphism implementation.............")
print(" ")

polyvehicleslist: list[VehiclePoly] = [
    NewPloyCar('new ford','focus new version',2010,8),
    NewPolyMotorcycle('Honda new version','Scoopy 1', 2020)
]

for vehicle in polyvehicleslist:
    if isinstance(vehicle, VehiclePoly):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    else:
        raise Exception("Object is not a valid vehicle")



