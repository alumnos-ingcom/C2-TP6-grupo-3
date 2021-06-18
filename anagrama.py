################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def anagrama(palabra1,palabra2):
    lista1 = list(palabra1)
    lista2 = list(palabra2)

    lista1.sort()
    lista2.sort()

    pos = 0
    isTrue = True

    while pos < len(palabra1) and isTrue:
        if lista1[pos]== lista2[pos]:
            pos = pos + 1
        else:
            isTrue = False

    return isTrue

def principal():
    palabra1 = input("Ingrese una palabra: ")
    palabra2 = input("Ingrese otra palabra: ")
    print(anagrama(palabra1,palabra2))

if __name__ == "__main__":
    principal()

