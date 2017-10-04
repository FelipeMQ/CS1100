import sys
import urllib
import http.cookiejar
import pprint
import numpy as np
from PIL import Image
from urllib import request
from urllib import parse

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')]
opener.addheaders = [('Upgrade-Insecure-Requests', '1')]
opener.addheaders = [('Referer', 'http://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/frameCriterioBusqueda.jsp')]
opener.addheaders = [('Origin', 'http://e-consultaruc.sunat.gob.pe')]
opener.addheaders = [('Host', 'e-consultaruc.sunat.gob.pe')]
opener.addheaders = [('Content-Type', 'application/x-www-form-urlencoded')]
opener.addheaders = [('Cache-Control', 'max-age=0')]
opener.addheaders = [('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')]
urllib.request.install_opener(opener)

req = urllib.request.Request("http://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/frameCriterioBusqueda.jsp")
resp = urllib.request.urlopen(req)
contents = resp.read()
urllib.request.urlretrieve("http://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/captcha?accion=image", "captcha.jpg")

x=Image.open('captcha.jpg','r')
x=x.convert('L')
y=np.asarray(x.getdata(),dtype=np.float64).reshape((x.size[1],x.size[0]))
y[y < 240] = 0

y=np.asarray(y,dtype=np.uint8)
w=Image.fromarray(y,mode='L')
w.save('captcha.jpg')

try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
img2txt = pytesseract.image_to_string(Image.open('C:\\Users\\randiel.melgarejo\\PycharmProjects\\CS1100\\free\\captcha.jpg'), lang='eng')
img2txt = img2txt.replace(" ","").upper()
print(img2txt)

data = urllib.parse.urlencode({'accion': 'consPorRuc',
                               'razSoc':'',
                               'nroRuc': '20100035392',
                               'nrodoc':'',
                               'contexto':'ti-it',
                               'tQuery':'On',
                               'search1':'20100035392',
                               'codigo': img2txt,
                               'tipdoc':'1',
                               'search2':'',
                               'coddpto':'',
                               'codprov':'',
                               'coddist':'',
                               'search3':''
                               })
data = data.encode('utf-8')
print(data)
reqquery = urllib.request.Request("http://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/jcrS00Alias", data)
resquery = urllib.request.urlopen(reqquery)
contentquery = resquery.read()
pprint.pprint(contentquery)
