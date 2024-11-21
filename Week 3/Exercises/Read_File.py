# A program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’

with open("poem.txt","r") as f:
    content = f.read()
    if ("twinkle" in content.lower()):
        print("The word twinkle is present in the content")
    else:
        print("The word twinkle is not present in the content")
