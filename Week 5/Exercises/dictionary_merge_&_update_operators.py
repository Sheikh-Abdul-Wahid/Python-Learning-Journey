# Use | when you need a new merged dictionary without changing the originals
# Example:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Merge the dictionaries
merged_dict = dict1 | dict2
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Original dictionaries remain unchanged
print(dict1)  # Output: {'a': 1, 'b': 2}
print(dict2)  # Output: {'b': 3, 'c': 4}


# Use |= when you want to update an existing dictionary in-place.
# Example:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Update dict1 in-place
dict1 |= dict2
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}
