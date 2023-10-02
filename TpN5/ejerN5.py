C=int
for i in range(10):
    num=float(input('ingrese numero: '))
    mul2=num//2
    if mul2==0:
        C+=1

print(f'Numeros multiplos de 2 son: ${C}')