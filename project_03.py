
# problem #3, install module of ur choice and use it
# pip3 install pyjokes


import pyjokes
jokes = pyjokes.get_joke()
print(jokes)



import pyttsx3
engine = pyttsx3.init()

# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say(jokes)
print(jokes)
# engine.say("thank you")
engine.runAndWait()