class Employee: # Parent class
    company = "IBM"
    name = "Alex"
    def show(self):
        print(f"The employee name is {self.name} working in {self.company} company")

# class Programmer():
#     company = "IBM Info"
#     def show(self):
#         print(f"The employee name is {self.name} working in {self.company} company")
    
#     def showLang(self):
#         print(f"The employee name is {self.name} and he is good with {self.language} language ")

# Instead of Repeating the above code for def show(self) both the class we can use inheritance method

class Programmer(Employee): # Child class (Inheritance) 
    company = "IBM Info"
    def showDetails(self): 
        print(f"The employee name is {self.name} and he is working in {self.company} company") # Here it takes the self.name from Parent class Employee


a = Employee()
b = Programmer()
print(a.company, b.company)
b.showDetails() 
