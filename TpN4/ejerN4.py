num1 = float(input('Ingrese  un numero: '))
num2 = float(input('Ingrese un numero: '))

rest = num1%num2 

if rest == 0:
    print(f'El numero {num1} es divisible por {num2}')
    
else:print(f'El numero {num1} no es divisible por {num2}')