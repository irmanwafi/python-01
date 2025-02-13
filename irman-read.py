class Car:
    def __init__(self, brand="ProtonSaga", color="Hitam"):
        self.brand = brand  # Store brand
        self.color = color  # Store color

    def show_info(self):
        print(f"\nRelax la weh kereta dia warna {self.color} je pun tapi tula brand {self.brand} ")

# Creating cars with different data


kereta1 = Car("ProtonX70", "Merah")
kereta2 = Car()
kereta1.show_info()
kereta2.show_info()

################### Separate Classes (No Connection)

class Car:
    def drive(self):
        print("The car is driving.")

class Bike:
    def ride(self):
        print("The bike is being ridden.")

class Bus:
    def stop(self):
        print("The bus has stopped.")

# Creating objects
car1 = Car()
bike1 = Bike()
bus1 = Bus()

car1.drive()  # Output: The car is driving.
bike1.ride()  # Output: The bike is being ridden.
bus1.stop()   # Output: The bus has stopped.

################### Inheritance ( Is a )

class Vehicle:  # Parent class
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(f"This is a {self.brand}.")

class Car(Vehicle):  # Inherits from Vehicle
    def drive(self):
        print(f"{self.brand} car is driving.")

class Bike(Vehicle):  # Inherits from Vehicle
    def ride(self):
        print(f"{self.brand} bike is being ridden.")

# Creating objects
car1 = Car("Toyota")
bike1 = Bike("Yamaha")

car1.show_brand()  # Output: This is a Toyota.
car1.drive()       # Output: Toyota car is driving.

bike1.show_brand() # Output: This is a Yamaha.
bike1.ride()       # Output: Yamaha bike is being ridden.


################### Composition (Has a)

class Engine:
    def start(self):
        print("Engine started.")

class Wheels:
    def rotate(self):
        print("Wheels are moving.")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car has an Engine
        self.wheels = Wheels()  # Car has Wheels

    def drive(self):
        self.engine.start()
        self.wheels.rotate()
        print("The car is driving.")

# Creating a car object
my_car = Car()
my_car.drive()

