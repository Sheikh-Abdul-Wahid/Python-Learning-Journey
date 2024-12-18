try:
    a = int(input("Enter a number: "))
    print(a)

except Exception as e:
    print(e)
    print("please enter integer and not string")
    
else:
    print("Inside else statement")
print("Thank You")
