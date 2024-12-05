# To handle the operations like (+,-,*,/) etc for the objects of the class we use overloading in python"

class Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(self,other):
        return self.a + other.a, self.b + other.b
    
    def __sub__(self,other):
        return self.a - other.a, self.b - other.b
    
    def __mul__(self,other):
        return self.a * other.a, self.b * other.b

x = Number(1,9)
y = Number(2,5)
print(x + y)
print(x - y)
print(x * y)
