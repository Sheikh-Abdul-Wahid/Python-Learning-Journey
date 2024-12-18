# This line checks whether a Python file is being run directly or imported as a module.
# It ensures that certain parts of code (like tests or main functions) run only when the script is executed directly.

def myFunction():
    print("Hello World!!")

if __name__ == "__main__": # we write this if statement so that it won't run the below code automatically while importing.
    print("We are directly running this code")
    myFunction()
    print(__name__)
