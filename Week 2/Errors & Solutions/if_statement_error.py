list_name = ["Abdul", "Wahid", "Sheikh"] # Define a list of names
name = input("Enter name: ") # Take user input for a name
print(list_name) # Print the list of names to show what is being checked

# Error: This compares the whole list to a single string, which is incorrect
if (name == list_name):
   print("Name is present in a list") # This block will not execute because a string cannot equal a list
else:
    print("Name is not present in a list")# This block will always execute, even if the name exists in the list

# Correct condition: "This checks if the value of the name exists as an element in the list
if (name in list_name):
   print("Name is present in a list")  
else:
    print("Name is not present in a list") 
