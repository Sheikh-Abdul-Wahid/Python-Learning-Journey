class Employee:
    language = "Python"
    salary = 1200000

    def getInfo(self):
        print(f"The language selected is {self.language} and the salary is {self.salary}")
    
    @staticmethod # This method doesnot require to use self parameter and it works perfect 
    def greet(): 
        print("Good Morning")

abdul = Employee()
# abdul.language = "Java"
abdul.greet()
abdul.getInfo()
