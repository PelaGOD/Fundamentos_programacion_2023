letra1= str(input('Ingrese un caracter: '))
letra2= str(input('Ingrese un caracter: '))
letra3= str(input('Ingrese un caracter: '))

if letra1<letra2 and letra1<letra3:
    print(f'la letra es {letra1}')
elif letra2<letra1 and letra2<letra3:
    print(f'la letra es {letra2}')
else:print(f'la letra es {letra3}')