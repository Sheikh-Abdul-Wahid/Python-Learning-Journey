# To avoid crashing of any program we explicitly print error rather than python throws any error, because if python throws any error then program will stop immeadiately and the remaining below code won't work. But if we explicitly print our own error then the below remaining code also works

# Example:
a = int(input("Enter a number: ")) # If I give any string input ex: abdul
print(a) # ValueError: invalid literal for int() with base 10: 'abdul'
print("Thank You") # This will not print after the crash

# Using Exception Handling:
try:
    a = int(input("Enter a number: "))
    print(a)

except Exception as e:
    print(e)
    print("please enter integer and not string")

# Or if we know specific error name then we can write below one as well:
except ValueError as v:
    print(v)
    print("please enter integer and not string")

print("Thank You") # Even after the error this will print
