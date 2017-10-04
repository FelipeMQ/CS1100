from gtts import gTTS
import os

tts = gTTS(text="""Bienvenido a Clarobot, 
has activado el bloqueo de linea, 
podemos validar tu identidad?""", lang='es')
tts.save("good.mp3")
os.system("mpg321 good.mp3")

tts = gTTS(text="""Cual es tu nombre completo?""", lang='es')
tts.save("good.mp3")
os.system("mpg321 good.mp3")

tts = gTTS(text="""Cual es tu numero de DNI?""", lang='es')
tts.save("good.mp3")
os.system("mpg321 good.mp3")

tts = gTTS(text="""Cual es tu numero de celular, por el cual llamas?""", lang='es')
tts.save("good.mp3")
os.system("mpg321 good.mp3")

tts = gTTS(text="""Gracias por validar tu informacion. 
Por favor confirmanos que quieres bloquear el numero 9 9 9 9 10 9 5 3.""", lang='es')
tts.save("good.mp3")
os.system("mpg321 good.mp3")

tts = gTTS(text="""Su numero ha sido bloqueado exitosamente. 
El numero de atencion es: 4 3 5 2 3.""", lang='es')
tts.save("good.mp3")
os.system("mpg321 good.mp3")

tts = gTTS(text="""Deseas escuchar las ofertas que tenemos para ti?.""", lang='es')
tts.save("good.mp3")
os.system("mpg321 good.mp3")