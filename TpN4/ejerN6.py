num1= float(input('Ingrese numero:'))
num2= float(input('Ingrese numero:'))

print(f'numeros al inicio {num1} y {num2}')
rest= num1%num2

if rest == 0:
    num=num1
    num1=num2
    num2=num
    print(f'intecambiados {num1} y {num2}')

else: print('los numeros no son divisibles')