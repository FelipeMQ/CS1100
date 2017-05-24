def main():
    alfa="EJOSZ"
    newa="3L025"
    mirr="AHIMOTUVWXY81"
    while True:
        try:
            lista = []
            valor = None
            while valor!="":
                valor = input()
                lista.append(valor)

        except EOFError:
            break
        except ValueError:
            break

        for palin in lista:
            convert = ""
            cntmirr = 0
            for cnt,c in enumerate(palin):
                print(cnt,len(palin) // 2)
                if mirr.count(c)>0 and cnt != len(palin) // 2:
                    cntmirr = 1
                if newa.count(c):
                    convert+=alfa[newa.index(c)]
                else:
                    convert+=c
            if palin == palin[::-1] and cntmirr==0:
                print(palin, "-- is a regular palindrome.")
            elif len(palin) % 2 == 1 and palin == palin[::-1] and (mirr.count(palin[len(palin) // 2]) > 0 or cntmirr == 1):
                print(palin, "-- is a mirrored palindrome.")
            elif convert == convert[::-1]:
                print(palin, "-- is a mirrored string.")
            else:
                print(palin, "-- is not a palindrome.")
            print()

if __name__ == '__main__':
    main()