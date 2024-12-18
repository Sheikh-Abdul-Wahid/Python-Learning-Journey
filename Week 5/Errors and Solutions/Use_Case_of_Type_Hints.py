# By using type hints in function definitions, we can make our code editor smarter. 
# Type hints not only act as documentation but also enable features like auto-suggestions, which reduces errors.

def concatenate(a: int, b: str):
    # Example usage inside the function
    result = b.upper()     # IDE suggests methods related to 'str' for 'b'
    return str(a) + result

output = concatenate(123, "hello") # Calling the function
print(output)                      # Output: "123HELLO"
