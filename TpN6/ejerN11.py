def DivTF(num1,num2):
    res=num1%num2
    res1=num2%num1
    if res==0 or res1==0:
        return print('Los numeros son divisible por el otro')
    else: return print('Los numeros no son divisibles')

numero1=int(input('ingrese numero: '))
numero2=int(input('ingrese un nuemro: '))

DivTF(numero1,numero2)