
import os
print(os.listdir())
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
volume = engine.getProperty ('volume')
engine.setProperty ('volume',1.0)
engine.setProperty('voice', voices[0].id) #1= Female voice 0-Default=Male
engine.say('''Hello! Prayaaan''')
engine.say('''Prisha is studying in Class 1, Air Force Golden Jubliee Institude''')
engine.runAndWait()

