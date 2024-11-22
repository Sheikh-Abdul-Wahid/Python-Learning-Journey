# Error Code:

with open("log.txt") as f:  # Open the file "log.txt" in read mode
    lines = f.readlines()   # Read all lines from the file into a list
line_no = 1                 # Initialize line number to 1

for line in lines:          # Loop through each line in the file
  if "python" in line:      # Check if the word "python" is present
        print(f"Yes, python is present in line number: {line_no}")
        # ERROR: The 'break' here stops the loop after finding the first occurrence,
        # so subsequent occurrences are not checked or printed.
        break
    line_no += 1           # Increment the line number for the next iteration
else:                      # If no occurrence was found, print a message
    print("No, python is not present")

# Coorect Code:

with open("log.txt") as f: # Open the file "log.txt" in read mode
    lines = f.readlines()  # Read all lines from the file into a list
line_no = 1                # Initialize line number to 1

# Initialize a flag to track if 'python' is found in any line
found = False
for line in lines:        # Loop through each line in the file
    if "python" in line:
        print(f"Yes, python is present in line number: {line_no}")
        found = True      # Set the flag to True when 'python' is found
    line_no += 1          # Increment the line number for the next iteration

# If the flag remains False, it means 'python' wasn't found in any line
if not found:
    print("No, python is not present")
