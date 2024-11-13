# while loop:
# A while loop is used when the number of iterations is not known beforehand, and 
# The loop should continue until a specific condition becomes false.

i = 0        # Initialize a counter variable 'i' with the value 0
while i < 5: # Start a while loop that runs as long as 'i' is less than 5
    print(i) # Print the current value of 'i'
    i += 1   # Increment 'i' by 1 to move to the next number


# for loop: 
# A for loop is used when you have a sequence (like a list, range, or string) to iterate over, or 
# when the number of iterations is predetermined.

names = ["Abdul", "Sheikh", "Rohan"] # Create a list of names
for name in names: # Use a for loop to iterate through each name in the list
   print(name)      # Print the current name
