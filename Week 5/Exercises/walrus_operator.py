# Example 1:
a = True
print(a = False) # Output: TypeError: print() got an unexpected keyword argument 'a'

# Using Walrus Operator:
a = True
print(a := False)

# Example 2:
numbers = [1,2,3,4,5]
while True:
    if len(numbers) > 0:
        print(numbers.pop())
    else:
        break

# Using Walrus Operator:
numbers = [1,2,3,4,5]
while (num:= len(numbers)) > 0: # Here "num" stores length of numbers & class is "int"
    print(numbers.pop())

        
# Example 3:
foods = []
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)
print(foods)

# Using Walrus Operator:
foods = []
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)
print(foods)
