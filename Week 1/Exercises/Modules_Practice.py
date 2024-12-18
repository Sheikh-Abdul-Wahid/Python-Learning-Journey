Question: Install an external module and use it to perform an operation of your interest.  

Solution:

import pyttsx3 #pyttsx3 is a Python library that allows users to convert text to speech

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the text to be spoken
engine.say('''Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.''')

# Start the speech process and wait for the completion
engine.runAndWait()
