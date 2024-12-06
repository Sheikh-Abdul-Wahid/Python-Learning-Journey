# I observed that when trying to add two Vector objects and print the result.
# The key here is that the __add__ method is returning a string directly, so it doesn’t need __str__ to display the result. 
# Since __add__ returns a string representation, Python automatically prints the result without needing the __str__ method.

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):  # Correctly add two vectors & return a string
        return f"({self.x + other.x}i + {self.y + other.y}j + {self.z + other.z}k)"

v1 = Vector(7, 8, 10)
v2 = Vector(7, 8, 10)
print(v1 + v2)        # This works as expected and prints the sum of the vector without __str__ method
                      # Output: (14i + 16j + 20k)
