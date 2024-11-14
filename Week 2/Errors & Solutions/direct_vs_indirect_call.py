# Explicit (Direct) Function Call:

def inch_to_cm(inch):  # Define a function that takes 'inch' as input
    cm = (2.54 * inch)  # Convert inches to centimeters
    print(f"{inch} inches = {cm} centimeters ")  # Print the result

inch = int(input("Enter value in inches: "))  # Get input from the user
inch_to_cm(inch)  # Directly call the function with the user's input

# Implicit (Indirect) Function Call:

def inch_to_cm(inch):  # Define a function that takes 'inch' as input
    return (2.54 * inch)  # Convert inches to centimeters & return the result

inch = int(input("Enter value in inches: "))  # Get input from the user
print(f"{inch} inches = {inch_to_cm(inch)} centimeters ") # Call the function & print the result
