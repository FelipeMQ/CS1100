nombre = "Pedro Pablo"
#Solución con programación estructurada
cc=0
cv=0
consonantes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','y','x','z']
vocales = ['a','e','i','o','u']
for c in nombre.lower():
    if c in consonantes:
        cc = cc + 1
    elif c in vocales:
        cv = cv + 1
print(cc, "consonantes")
print(cv, "vocales")