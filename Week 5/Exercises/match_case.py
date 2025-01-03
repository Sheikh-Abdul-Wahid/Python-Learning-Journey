# The match-case construct (introduced in Python 3.10) is Python’s version of a pattern-matching mechanism. 
# It provides a powerful and expressive way to handle complex conditional logic, often replacing cumbersome if-elif chains.
# Before match-case, handling multiple conditions (especially for structured data) required lengthy if-elif chains, which were less readable and harder to maintain.
# Python lacked a direct equivalent of a switch-case statement, which is common in other languages like C, Java, or JavaScript.

# Replacing Long if-elif Chains:
# Example:

def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"  # Default case (like 'else')
        
print(http_status(500))
        
