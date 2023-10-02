cadena1=str(input('ingrese cadena: '))
cadena2=str(input('ingrese cadena: '))

a=len(cadena1)
b=len(cadena2)

def condicion(a,b):
    if a>b:
        return print('la cadena 1 es mas larga')
    elif a<b:
        return print('la cadena 2 es mas larga')
    else:return print('las cadenas son del mismo tamaño')

condicion(a,b)