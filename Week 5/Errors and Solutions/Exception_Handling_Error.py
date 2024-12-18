# A division by zero raises a ZeroDivisionError, but I mistakenly tried to catch a ValueError.
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ValueError:  # Incorrect exception type
     print("You cannot divide by zero!")

# Solution:

try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:  # Correct exception type
    print("You cannot divide by zero!")
  
# Output: You cannot divide by zero!
