import pyttsx

def onStart(name):
    print("iniciando",name)
def onWord(name, location, length):
    print("palabra",name, location, length)
    #if location>15:
        #engine.stop()
def onEnd(name, completed):
    print("fin", name, completed)

engine = pyttsx.init()
engine.connect("started-utterance", onStart)
engine.connect("started-word", onWord)
engine.connect("finished-utterance", onEnd)

engine.say('Primera pronunciación.')
engine.say('Segunda pronunciación.')
engine.runAndWait()

