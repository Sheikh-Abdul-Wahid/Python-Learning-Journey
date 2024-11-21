class Employee:
    language = "Python"
    salary = 1200000

    def __init__(self, name, language, salary):
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating an object")
        
        
    def getInfo(self):
        print(f"The language selected is {self.language} and the salary is {self.salary}")
    
    @staticmethod # This method doesnot require to use self paramter and it works perfect 
    def greet(): 
        print("Good Morning")

abdul = Employee("Abdul", "Java", 1300000)
print(abdul.name, abdul.language, abdul.salary)
