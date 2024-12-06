# Problem: Calling super().__init__() without passing the required arguments to the parent class, which caused this error.

class TwoDvector:  # Parent class
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The 2-D vector is: {self.i}i + {self.j}j")

class ThreeDvector(TwoDvector):  # Child class (Inheritance)
    def __init__(self, i, j, k):
        super().__init__()       # Error: Missing arguments for parent class
        self.k = k

    def show(self):
        print(f"The 3-D vector is: {self.i}i + {self.j}j + {self.k}k")

b = ThreeDvector(5, 8, 7)  # This will raise a TypeError
print(b.i, b.j, b.k)
b.show()                   # TypeError: TwoDvector.__init__() missing 2 required positional arguments: 'i' and 'j'

# Solution: Pass the necessary arguments (i and j) to the parent class using the super() method.

class TwoDvector:                # Parent class
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The 2-D vector is: {self.i}i + {self.j}j")

class ThreeDvector(TwoDvector):  # Child class (Inheritance)
    def __init__(self, i, j, k):
        super().__init__(i, j)   # Pass i and j to the parent class
        self.k = k

    def show(self):
        print(f"The 3-D vector is: {self.i}i + {self.j}j + {self.k}k")
                      
b = ThreeDvector(5, 8, 7)       # Now works correctly
print(b.i, b.j, b.k)            # Output: 5 8 7
b.show()                        # Output: The 3-D vector is : 5i + 8j + 7k
