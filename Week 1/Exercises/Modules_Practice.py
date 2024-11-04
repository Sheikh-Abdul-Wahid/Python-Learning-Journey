import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the text to be spoken
engine.say('''Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.''')

# Start the speech process and wait for completion
engine.runAndWait()
