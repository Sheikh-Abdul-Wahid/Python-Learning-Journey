class Employee:
    a = 5
    @classmethod
    def show(cls):
        print(f"The class attribute value is {cls.a}")

e = Employee()
e.a = 9  # instance attribute
e.show() # This shows a value 9 because of instance attribute preference over class attribute 
         # but by using @class method we can change the preference to class attribute
