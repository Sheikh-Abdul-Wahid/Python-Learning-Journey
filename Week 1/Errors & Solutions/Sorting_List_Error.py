Problem: 
I wrote a program to sort user inputs, but the sort () function treated the inputs as strings instead of numbers, 
causing incorrect alphabetical sorting."

# Create an empty list to store marks
marks = []

m1 = input("Enter marks of first student: ")
marks.append(m1) # Add first student's marks to the list

m2 = input("Enter marks of second student: ")
marks.append(m2)  # Add second student's marks to the list

m3 = input("Enter marks of third student: ")
marks.append(m3)  # Add third student's marks to the list

# Sort the marks in ascending order (this will sort them alphabetically, not numerically, due to string input)
marks.sort()

# Print the sorted marks
print("Marks in sorted order:", marks)

Solution: Use int function while taking input, ensuring each mark was stored as an integer. 

# Create an empty list to store marks
marks = []

# Get marks from the first student and convert to integer
m1 = int(input("Enter marks of first student: "))
marks.append(m1)  # Add first student's marks to the list

m2 = int(input("Enter marks of second student: "))
marks.append(m2)  

m3 = int(input("Enter marks of third student: "))
marks.append(m3)  

# Sort the marks in ascending order (now sorted numerically)
marks.sort()

# Print the sorted marks
print("Marks in sorted order:", marks)
