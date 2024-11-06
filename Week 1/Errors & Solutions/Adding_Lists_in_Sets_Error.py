# Attempting to add a list to a set
s = {8, 7, 12, "Abdul", [1, 2]} # This will raise an error

# TypeError: unhashable type: 'list'

Solution:

# Using a tuple instead of a list
s = {8, 7, 12, "Abdul", (1, 2)}
print(s)  

# Output: {8, 7, 12, 'Abdul', (1, 2)}

If you need a different tuple, you can remove the existing one and add a new tuple.

# Using a tuple instead of a list
s = {8, 7, 12, "Abdul", (1, 2)}
s.remove((1, 2))  # Remove the original tuple
s.add((3, 4))     # Add a new tuple with modified values
print(s)

# Output: {'Abdul', (3, 4), 7, 8, 12}
