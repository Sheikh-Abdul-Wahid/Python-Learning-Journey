Question: Write a program to fill in a letter template given below with name and date. 
          letter = '''  Dear <|Name|>, 
          You are selected! 
          <|Date|> ''' 

Solution:

name = input("Enter name: ")
date = input("Enter Date: ")

letter =f'''  
Dear {name}, 
You are selected! 
{date}''' 

print(letter)

(OR)

letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> ''' 

print(letter.replace("<|Name|>","Abdul").replace("<|Date|>","25 September 2024"))

Output:
Dear Abdul, 
You are selected!
25 November 2024
