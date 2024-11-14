# Error Code:
def factorial(n):
    return n * factorial(n - 1) # No base case, recursion goes on indefinitely
n = int(input("Enter the Number: "))
print(f"The Factorial of {n} is {factorial(n)}")
# RecursionError: maximum recursion depth exceeded

# Correct Code:
def factorial(n):
    if (n == 1 or n == 0):  # Base case: factorial of 0 or 1 is 1
        return 1
    return n * factorial(n - 1)  # Recursive call
n = int(input("Enter the Number: "))  # Get input from the user
print(f"The Factorial of {n} is {factorial(n)}")  # Print the result
