# Incorrect import
import maths
"Error: Module 'maths' not found. Did you mean 'math'?"

# Correct import
import math
print(math.pi) # Output:3.141592653589793

# Incorrect
print(math.pi)
NameError: name 'math' is not defined

# Solution
import math
print(math.pi) # Output:3.141592653589793

from math import pi
print(pi) # Output:3.141592653589793

import math as m
print(m.pi) # Output:3.141592653589793
