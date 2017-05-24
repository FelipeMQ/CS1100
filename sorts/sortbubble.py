def bubblesort(list):
    cnt=0
    for p in range(len(list)-1,0,-1):
        if cnt==3:
            break;
        for i in range(p):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i]=list[i+1]
                list[i+1]=temp
        cnt = cnt + 1
    return lista
lista = [19,1,9,7,3,10,13,15,8,12]
print(bubblesort(lista))