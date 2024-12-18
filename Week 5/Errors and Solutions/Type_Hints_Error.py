# Error Code:
def add_numbers(a: int, b: int) -> int:
    return a + b

result = add_numbers(5, "10")  # Passing an integer and a string
# Output: TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Solution Code:

def add_numbers(a: int, b: int) -> int:
    # Validate input types
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")
    return a + b

result = add_numbers(5, 10)  # Passing correct types
print(result)                # Output: 15

# Passing incorrect types (e.g., add_numbers(5, "10")) will raise a clear error message:
# Output: TypeError: Both arguments must be integers
