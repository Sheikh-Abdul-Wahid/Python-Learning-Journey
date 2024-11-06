# Creating a tuple
my_tuple = (1, 2, 3)

# Trying to modify a tuple (this will raise an error)

my_tuple [0] = 10
print(my_tuple) # Output: Error: 'tuple' object does not support item assignment

# Correct approach if you need a modifiable collection
my_list = [1, 2, 3]
my_list [0] = 10 # Lists can be modified
print(my_list) # Output: [10, 2, 3]
