import time

cancion = """Oh no...
Oh no...
¡Hey!
Si, sabes que ya llevo y un rato mirándote
tengo que bailar contigo hoy
vi, que tu mirada ya estaba llamándome
muéstrame el camino que yo voy

Tu
tu eres el imán y yo soy el metal
me voy acercando y voy armando el plan
solo con pensarlo se acelera el pulso

Ya
ya me esta gustando más de lo normal
todos mis sentidos van pidiendo más
esto hay que tomarlo sin ningún apuro

Despacito
quiero respirar tu cuello despacito
deja que te diga cosas al oído
para que te acuerdes si no estas conmigo

Despacito
quiero desnudarte a besos despacito
firmar las paredes de tu laberinto
y hacer de tu cuerpo todo un manuscrito

Quiero ver bailar tu pelo
quiero ser tu ritmo
que le enseñes a mi boca
tus lugares favorito

Déjame sobre pasar
tus zonas de peligro
hasta provocar tus gritos
y que olvides tu apellido

Si te pido un beso, ven dámelo
yo se que estas pensándolo
llevo tiempo intentándolo
mami esto es dando y dándolo
sabes que tu corazón conmigo
te hace boom boom
sabes que esa beba esta buscando
de mi baam baam

Ven prueba de mi boca, para ver como te sabe
quiero quiero quiero, ver cuanto amor a ti te cabe
yo no tengo prisa, yo me quiero dar el viaje
empezamos lento, después salvaje

Pasito a pasito, suave suavecito
nos vamos pegando, poquito a poquito
cuando tu me besas, con esa destreza
creo que eres malicia, con delicadesa

Pasito a pasito, suave suave cito
nos vamos pegando, poquito a poquito
y es que esa belleza, es un rompecabezas
pero para montalo aquí tengo la pieza, oye..

Despacito
quiero respirar tu cuello despacito
deja que te diga cosas al oído
para que te acuerdes si no estas conmigo

Despacito
quiero desnudarte despacito
firmar las paredes de tu laberinto
y hacer de tu cuerpo todo un manuscrito

Quiero ver bailar tu pelo
quiero ser tu ritmo
que le enseñes a mi boca
tus lugares favoritos

Déjame sobre pasar
tus zonas de peligro
hasta provocar tus gritos
y que olvides tu apellido

Despacito
vamos hacerlo en un playa en puertorrico
hasta que las olas griten, ay bendito
para que mi sello se quede contigo,

Pasito a pasito, suave suavecito
nos vamos pegando, poquito a poquito
que le enseñes a mi boca
tus lugares favoritos,

Pasito a pasito, suave suavecito
nos vamos pegando, poquito a poquito
hasta provocar tus gritos y que
y que olvides tu apellido, Des pa cito

Pasito a pasito, suave suavecito
nos vamos pegando, poquito a poquito
eh, eh , eh, eh...
Pasito a pasito, suave suavecito
nos vamos pegando, poquito a poquito
eh, eh , eh, eh...""".splitlines()

cancion = """Oh no...
Oh no...
¡Hey!
Si, sabes que ya llevo un rato mirándote
tengo que bailar contigo hoy
""".splitlines()

delay = 500
letra=[]
cadena = ""
for artemayor in cancion:
    letra.append(artemayor)

karaoke=[]
letrakaraoke = []
marca=[]
marca.append([1,1])
marca.append([1,5])
marca.append([6])
marca.append([2,0.5,0.5,0.5,0.5,0.5,0.5,6])
marca.append([1,1,1,2,1])

inicio=[]
inicio.append("0:34")
inicio.append("0:35")
inicio.append("0:38")
inicio.append("0:41")
inicio.append("0:46")

cnt=0
for artemayor in letra:
    lchar = artemayor.split(" ")
    cnv=0
    karaoke = []
    for silaba in lchar:
        karaoke.append([silaba,marca[cnt][cnv]])
        cnv+=1
    letrakaraoke.append([inicio[cnt], karaoke])
    cnt += 1
    #for char in artemayor:

ind=0
for pulse,letrapulse in letrakaraoke:
    print(pulse, flush=True, end=" >> ")
    for letra in letrapulse:
        print(letra[0],letra[1], flush=True, end=" ")
        time.sleep(letra[1] * delay / 1000)
    ind+=1
    print("")
