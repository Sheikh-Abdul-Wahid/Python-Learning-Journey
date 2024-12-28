# Using List Comprehension:
l = [1, 2, 3, 4, 5]
sqlist = [item * item for item in l]
print(sqlist)

# Using Map Example:
l = [1, 2, 3, 4, 5]

square = lambda x : x*x
squarelist = map(square,l)
print(list(squarelist))

# Filter Example:
l = [1,2,3,4,5,6,7,8,9,10]

def even(n):
    if (n%2 == 0):
        return True
    return False    

even_list = filter(even,l)
print(list(even_list))

# Reduce Example: 
from functools import reduce
l = [1,2,3,4]

def sum(a,b):
    return a+b
sum_list = reduce(sum,l)
print(sum_list)

multiply = lambda x,y : x*y
mul_list = reduce(multiply,l)
print(mul_list)
