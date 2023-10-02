def factorial(numero):
    result=1
    if numero==0:
        result=1
    else:
        for i in range(1,numero):
            result=result*i
    return print(f'el factorial de {numero} es {result}')

num=int(input('Ingrese el numero a factoriar:'))

factorial(num)