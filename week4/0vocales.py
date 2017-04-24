#Problema: Contar vocales y consonantes
#input
nombre = "Pedro Pablo"
#Solución con programación estructurada
cc=0
cv=0
for c in nombre.lower():
    if "bcdfghjklmnñpqrstvwxyz".count(c)>0:
        cc = cc + 1
    elif "aeiouáéíóúäëïöü".count(c)>0:
        cv = cv + 1
print(cc, "consonantes")
print(cv, "vocales")

#Problema: Contar vocales y consonantes
#input
nombre = "Pedro Pablo"
#Solución con programación funcional
lcc = len(list(filter(lambda x:"bcdfghjklmnñpqrstvwxyz".count(x)>0,nombre.lower())))
lcv = len(list(filter(lambda x:"aeiouáéíóúäëïöü".count(x)>0,nombre.lower())))
print(lcc, "consonantes")
print(lcv, "vocales")