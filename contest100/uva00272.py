import re

def main():
    while True:
        try:
            cadena = input()
            replaced = re.sub("([\"])([\"])","\$$\%%",cadena)
            print(replaced)
        except EOFError:
            break
        except ValueError:
            break

if __name__ == '__main__':
    main()