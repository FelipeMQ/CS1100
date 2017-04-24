#filas = int(input())
#cnt = 0
#Alph = "A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z "
#while cnt<=filas:
#    print(" "*(filas-cnt)+Alph[0:cnt*2])
#    cnt=cnt+1

x=int(input())
if 1<=x<=27:
  strg="A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z "[:(x*2)]
  i = 0
  c = 1
  while i < len(strg):
     print (" "*(x-c), strg[0:i+2], sep="")
     i = i+2
     c = c+1
else:
  print("Valor incorrecto")