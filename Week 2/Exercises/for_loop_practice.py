# Example: 5! = 1 X 2 X 3 X 4 X 5

n = int(input("Enter the number: "))

fact = 1
for i in range(1, n+1):
    fact = fact * i

print(f"The factorial of {n} is {fact}")
