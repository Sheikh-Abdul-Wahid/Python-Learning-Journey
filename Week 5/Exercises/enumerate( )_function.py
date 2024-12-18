# Enumerate function adds counter to an iterable and returns it.
# Without enumerate function:

lst = [1,5,3,89,69,78]
index = 0
for item in lst:
    print(f"The item number at index {index} is {item}")
    index += 1

# Using enumerate function:
lst = [1,5,3,89,69,78]

for index, item in enumerate(lst):
    print(f"The item number at index {index} is {item}")

# Using enumerate function with index value = 1:
lst = [1,5,3,89,69,78]

for index, item in enumerate(lst, start=1):
    print(f"The item number at index {index} is {item}")
