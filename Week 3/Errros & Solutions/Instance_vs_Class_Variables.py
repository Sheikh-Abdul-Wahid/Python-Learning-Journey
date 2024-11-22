class Car:      # Class variable (shared by all instances)
    wheels = 4  # All cars have 4 wheels by default

    def __init__(self, make, model): # Instance variables (specific to each car)
        self.make = make
        self.model = model

# Create two Car objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Accessing class variable (same for all cars)
print(car1.wheels)  # Output: 4
print(car2.wheels)  # Output: 4

# Accessing instance variables (unique for each car)
print(car1.make)  # Output: Toyota
print(car2.make)  # Output: Honda
