num = float(input('Ingrese el numero: '))

rest = num%5

if rest == 0:
    print(f'El numero {num} es multiplo de 5')
else:print(f'El numero {num} no es multiplo de 5')