cont=0
par=int
for i in range(300,1232):
    par=i%2
    if par==0:
        cont=cont+i

print(f'la suma de numeros pares es {cont}')