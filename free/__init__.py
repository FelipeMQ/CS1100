import pycurl
from io import BytesIO

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/captcha?accion=image')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
# Body is a byte string.
# We have to know the encoding in order to print it to a text file
# such as standard output.
print(body.decode('iso-8859-1'))


def comb(n, m):
    if n < 1 or m < 1 or n > 1000 or m > 1000:
        print("Valor incorrecto")
    else:
        print(fact(n) // (fact(m) * fact(n - m)))


def fact(k):
    if k == 1:
        return 1
    else:
        return k * fact(k - 1)


#n, m = input().split(",")
#n = int(n)
#m = int(m)
#comb(n,m)
#print((2, 2, 2) == (2, 2, 2))
#print(max("dddd","sdsdfd"))

