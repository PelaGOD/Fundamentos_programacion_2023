num = int(input('Ingrese numero: '))
rest=0
for i in range(1,num):
    rest=(1/i)+rest

print(f'el resultado es : {rest}')