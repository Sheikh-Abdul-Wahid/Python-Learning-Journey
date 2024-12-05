class Employee:
    company = "Microsoft"
    region = "London"
    def details(self):
        print(f"The employee works in {self.company}")

class Programmer(Employee):
    language = "Python"
    def newDetails(self):
        print(f"The employee works in {self.company} and his region is {self.region} who uses {self.language} language")

class Manager(Programmer):
    def showDetails(self):
        print(f"The employee works in {self.company} and his region is {self.region} who uses {self.language} language")

o = Employee()
a = Programmer()
b = Manager()
print(o.company, a.language, b.region)
b.showDetails()
