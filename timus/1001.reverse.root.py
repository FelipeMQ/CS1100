import math

valores = []

while True:
    line = input()
    if line:
        valores.append(" ".join(line.split(" ")))
    else:
        break
text = " ".join(valores).split(" ")

for it in text:
    if (it!=""):
        print("%.4f" % math.sqrt(int(it)))
