# Error Code:
for i in range(10):  # Loop through numbers from 0 to 9
    print(i)  # It prints the current number before checking the condition
    if (i == 5):  # Check if the current number is 5
        continue  # Error: continue is placed after print(), so 5 is still printed before skipping.

# Correct Code:
for i in range(10):  # Loop through numbers from 0 to 9
    if i == 5:  # Check if the current number is 5
        continue  # Skip iteration of 5 and continue to next one
    print(i)  # Print the current number only if it is not skipped
