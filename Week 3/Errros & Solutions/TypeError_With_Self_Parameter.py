# Error Code:

class Employee:
    language = "Python"
    salary = 1200000

   def getInfo():  # Missing 'self' as the first parameter
        print(f"The language selected is {language} and the salary is {salary}")

abdul = Employee() # Create an instance of Employee
abdul.getInfo()    # Call the getInfo method on the instance

# TypeError: Employee.getInfo() takes 0 positional arguments but 1 was given

# Correct Code:

class Employee:
    language = "Python"
    salary = 1200000

   def getInfo(self):  # Correct method definition with 'self'
        print(f"The language selected is {self.language} and the salary is {self.salary}")

abdul = Employee() # Create an instance of Employee
abdul.getInfo()    # Call the getInfo method on the instance

# Output: The language selected is Python and the salary is 1200000
