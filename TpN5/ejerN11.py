C1=0
C2=0
C3=0

for i in range(1,50):

    y=float(input('ingrese el valor de y: '))
    x=float(input('ingrese el valor de x: '))
    if x>y:
        C1=C1+1
    elif x<y:
        C2=C2+1
    else:C3=C3+1

print(f'Cantidad de numeros X mayores:{C1}')
print(f'Cantidad de numeros Y mayores:{C2}')
print(f'Cantidad de numeros pares:{C3}')