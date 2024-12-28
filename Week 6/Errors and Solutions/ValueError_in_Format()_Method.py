# Error Code:
a = "{} is a good {0}".format("Boy","Abdul")
print(a)

# Output: 
ValueError: cannot switch from automatic field numbering to manual field specification

# Solution: Use {1} for the first placeholder and {0} for the second one, so that the order of names in the .format() method gets switched.

a = "{1} is a good {0}".format("Boy", "Abdul") # Manual Field Numbering
print(a)

# OR

a = "{} is a good {}".format("Abdul","Boy") # This is default Automatic Field Numbering
print(a)

# Output: 
Abdul is a good Boy
