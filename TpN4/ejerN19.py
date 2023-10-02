num = float(input('ingrese numero: '))

if num>=23 or num<=54:
    res=num//3
    res1=num//5
    if res==0 or res1==0:
        print(f'el numero {num} es multiplo de 3 o 5')