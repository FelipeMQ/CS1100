import pyttsx

engine = pyttsx.init()
rate = engine.getProperty("rate")
engine.setProperty("rate", rate - 150)
engine.say("Centro de excelencia en mineria de datos...")
engine.runAndWait()