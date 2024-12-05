class Employee:
    company = "Microsoft"
    region = "London"
    def details(self):
        print(f"The employee works in {self.company}")

    def __init__(self):
        print("Constructor of class Employee")

class Programmer(Employee):
    language = "Python"
    def newDetails(self):
        print(f"The employee works in {self.company} and his region is {self.region} who uses {self.language} language")

    def __init__(self):
        print("Constructor of class Programmer")

class Manager(Programmer):
    def showDetails(self):
        print(f"The employee works in {self.company} and his region is {self.region} who uses {self.language} language")

    def __init__(self):
        super().__init__() # This will also call init of its parent class so no need to write __init__ of class Programmer 
                           # Also This method must be written inside def init of child class 
        print("Constructor of class Manager")
        
c = Manager()
