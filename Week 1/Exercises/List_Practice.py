Question: Write a program to store seven fruits in a list entered by the user.

Solution: 

fruits = []
f1 = input("Enter fruit name: ")
fruits.append(f1)
f2 = input("Enter fruit name: ")
fruits.append(f2)
f3 = input("Enter fruit name: ")
fruits.append(f3)
f4 = input("Enter fruit name: ")
fruits.append(f4)
f5 = input("Enter fruit name: ")
fruits.append(f5)
f6 = input("Enter fruit name: ")
fruits.append(f6)
f7 = input("Enter fruit name: ")
fruits.append(f7)
print(fruits)

# OR

fruits = []

for i in range(7):
    fruit = input("Enter fruit name: ")
    fruits.append(fruit)

print(fruits)
