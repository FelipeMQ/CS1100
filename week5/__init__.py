print("demo","dos",sep="")

n=int(input())
cnt=0
suma=0
val=0
while cnt<n:
    val=val+1
    if val % 2 ==0:
        cnt=cnt+1
        suma=suma+val
        if cnt<n:
            print(val,end='+')
        else:
            print(val, end='=')
print(suma)