# Error Code:

num = int(input("Enter the number to multiply: "))
lst = []
for item in range(1,11):
    lst.append(num*item)
print(lst)

string = "\n".join(lst)
print(string)

# Output: 
Enter the number to multiply: 5
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50] # List of Integers
TypeError: sequence item 0: expected str instance, int found

# Solution: To fix this error, I converted each result in the list lst into a string before using the join() method.

num = int(input("Enter the number to multiply: "))
lst = []
for item in range(1, 11):
    lst.append(str(num * item))  # Convert the result to string
print(lst)

string = "\n".join(lst)  # Join the list of strings with newlines
print(string)

# Output:
Enter the number to multiply: 5
['5', '10', '15', '20', '25', '30', '35', '40', '45', '50'] # List of String
5
10
15
20
25
30
35
40
45
50
