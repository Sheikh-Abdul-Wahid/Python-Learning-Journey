# Error Code:

x = 10            # Global variable
if (x := 5) > 3:  # Assigns 5 to `x` using the Walrus operator
    print(x)      # Output: 5

print(x)          # Output: 5 (Global `x` is overwritten)

# Solution Code:

x = 10            # Global variable
if (y := 5) > 3:  # Use a different variable name
    print(y)      # Output: 5

print(x)          # Output: 10 (Global `x` is not overwritten)
