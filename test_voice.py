import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('volume', 1)
engine.setProperty('rate', 135)
engine.setProperty('voice', voices[0].id)
engine.say("Pouvez-vous m'aider s'il vous plaît")
engine.runAndWait()
