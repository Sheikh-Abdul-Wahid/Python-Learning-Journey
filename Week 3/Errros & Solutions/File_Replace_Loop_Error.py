# Error Code:

words = ["Donkey", "Animal", "bad"]

with open("file.txt") as f:   # Open the file and read the content
    text = f.read()

for word in words: 
    newtext = text.replace(word, "#" * len(word))  # Replacing using the original text each time

with open("file.txt", "w") as f: # Write the updated text back to the file
    f.write(newtext)             # Only the last word gets replaced

'''
Output:
Donkey is a herbivorous animal. 
Donkey is not a ### animal.
Donkey carries load. 
'''

# Correct Code:

words = ["Donkey", "Animal", "bad"]

with open("file.txt") as f: # Open the file and read the content
    text = f.read()

for word in words: 
    text = text.replace(word, "#" * len(word))  # Update text with the new replacement

with open("file.txt", "w") as f: # Write the fully updated text back to the file
    f.write(text)                # All words are replaced properly
'''
Output:
###### is a herbivorous animal. 
###### is not a ### animal.
###### carries load. 
'''
