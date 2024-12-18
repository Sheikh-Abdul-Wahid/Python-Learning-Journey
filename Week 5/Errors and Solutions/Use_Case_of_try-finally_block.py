# Code Example (Without finally):

def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return  # Function returns here
    except Exception as e:
        print(e)
        return  # Function also returns here

    print("Goodbye!") # This statement will never be executed due to the `return` above

main()

# Code Example (With finally):

def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return  # Function returns here, but `finally` still executes
    except Exception as e:
        print(e)
        return  # Even if this executes, `finally` will still run
    finally:
        print("Goodbye!")  # This will always execute, regardless of `return`

main()
