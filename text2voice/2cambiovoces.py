import pyttsx

engine = pyttsx.init()
voices = engine.getProperty("voices")
for voice in voices:
    engine.setProperty('voice',voice.id)
    engine.say("Tell me how much time!")
engine.runAndWait()