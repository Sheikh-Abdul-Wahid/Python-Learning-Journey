# Problem: To print only one object value then only using def __add__(self) gives just a memory address, not the actual values.

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self):
        return Vector(self.x + self.y + self.z)
v = Vector(7,8,10)
print(v)   # Output: <__main__.Vector object at 0x000001AA02B96F90>

# Solution: To print the value in a readable format, I need to use def __str__(self) method.

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self):  # Correctly adds two vectors
        return Vector(self.x + self.y + self.z)
    def __str__(self):  # Used to return a string representation of the object. 
        return f"{self.x}i + {self.y}j + {self.z}k"
    
v = Vector(7,8,10)
print(v)                # Output: 7i + 8j + 10k
