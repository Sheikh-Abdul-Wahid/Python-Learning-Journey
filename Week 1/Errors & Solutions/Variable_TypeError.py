a = 1
b = 2
c = "Abdul"
print(a + b + c)

**Output:**
TypeError: unsupported operand type(s) for +: 'int' and 'str'

Solution: Convert Integers to Strings and then Concatenate

a = 1
b = 2
c = "abdul"

# Convert integers to strings before concatenation
result = str(a) + str(b) + c
print(result)  # Output: 12abdul
