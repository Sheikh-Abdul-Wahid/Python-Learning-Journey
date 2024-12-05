class Employee: # Parent class
    company = "IBM"
    name = "Alex"
    def show(self):
        print(f"The employee name is {self.name} working in {self.company} company")

class Coder:  # Parent class
    language = "Python"
    def showLang(self):
        print(f"The coder is very good at this language: {self.language}")

class Programmer(Employee, Coder): # Child class (Multiple Inheritance) 
    company = "IBM Info"
    def showDetails(self): 
        print(f"The employee name is {self.name} and he is good with {self.language} language working in {self.company} company") # Here it takes name and language from parent class

c = Programmer()
c.showDetails() # This prints everything taking attributes from Employee & Coder class and also we are not required to add objects for the previous two classes i.e Employee and Coder
