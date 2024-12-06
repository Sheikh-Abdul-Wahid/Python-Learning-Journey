# Problem: An instance attribute shadowing a class attribute, causing unexpected behavior

class Employee:
    a = 5
    @classmethod
    def show(cls):
        print(f"The value of a is: {cls.a}")
x = Employee()
x.a = 10
print(x.a)  # Prints 10 (instance attribute)
x.show()    # Prints 5 (class attribute)

# Solution: I ensured the attribute always referred to the class-level value by using the class name to directly refer to the class attribute

class Employee:
    a = 5
    @classmethod
    def show(cls):
        print(f"The value of a is: {cls.a}")
x = Employee()
x.a = 10
print(Employee.a)  # Prints 5, always uses the class attribute
x.show()           # Prints 5 (class attribute)
