# Global variable

x = 10

def my_function(y):  # y is a local variable (function parameter)
    z = 20  # z is a local variable
    print("Inside function:", x, y, z)

my_function(5)
# Trying to access local variable outside function

print(z)

