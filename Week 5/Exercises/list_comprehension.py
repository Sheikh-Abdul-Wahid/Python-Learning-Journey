# List Comprehension is an elegant way to create lists based on existing lists. 
# List comprehension is just a quick way to make a new list by writing a single line of code instead of a long for loop. 
# It’s like a shortcut to take items from one list (or another collection), change them if needed, and put them into a new list.

# Without list comprehension
mylist = [1,2,9,4,7]
squaredList = []
for item in mylist:
    squaredList.append(item * item)
print(squaredList)

# Using list comprehension
mylist = [1,2,9,4,7]
squaredList = [item * item for item in mylist]
print(squaredList)
