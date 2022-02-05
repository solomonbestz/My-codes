import pyttsx3
    
engine = pyttsx3.init()

voices =  engine.getProperty('voices')
rate = engine.getProperty('rate')

engine.setProperty('rate', 180)
engine.setProperty('voice', voices[0].id)

# for n in range(len(new_read)):
with open("TextToSpeech/lecture5.txt", "r") as f:
    engine.say(f.read().replace(".", ")."))
    engine.runAndWait()
