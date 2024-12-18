# While using the enumerate() function, It is a common mistake to forget to write index for the first element, 
# which leads to the generation of tuple values as the output.

fruits = ["apple", "banana", "cherry"]

# Forgetting to unpack the tuple returned by enumerate()
for fruit in enumerate(fruits):
    print(fruit)

# Output: 
'''
(0, 'apple')
(1, 'banana')
(2, 'cherry') '''

# Solution: Unpack the tuple into two variables: one for the index and the other for the value.

fruits = ["apple", "banana", "cherry"]

# Unpacking the tuple returned by enumerate()
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Output:
'''
0: apple
1: banana 
2: cherry  '''
