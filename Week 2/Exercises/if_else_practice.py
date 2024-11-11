marks1 = int(input("Enter Subject 1 marks: "))
marks2 = int(input("Enter Subject 2 marks: "))
marks3 = int(input("Enter Subject 3 marks: "))

total_percentage = int(((marks1 + marks2 + marks3)/300)*100)

if(total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33 ):
    print("Student Passed, Percentage:", total_percentage)

else:
    print("Student Failed, Percentage:", total_percentage)
