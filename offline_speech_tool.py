import pyttsx3 as pyttsx 
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
engine.say('how are you doing?')
engine.setProperty('rate', rate-100)
engine.say('how are you doing?')
engine.runAndWait()
