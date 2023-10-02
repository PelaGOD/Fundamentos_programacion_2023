m15=int
m24=int
m50 = int

for i in range(10):
    num=int(input('Ingrese numero: '))
    
    if num==15:
        m15=m15+1
    if num>=25 or num<=45:
        m24=m24+1
    if num>50: 
        m50=m50+1

print(f'la cantidad de numeros mayores 15 son : ${m15}')
print(f'la cantidad de numeros mayores 25 y menores 45 son : ${m24}')
print(f'la cantidad de numeros mayores 50 son : ${m50}')
