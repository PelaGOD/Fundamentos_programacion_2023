num= float(input('ingrese el numero: '))
con= str(input('ingrese operador (+,-,*,/): '))
num1= float(input('ingrese el numero: '))

if con=='+':
    res=num+num1
    print(f'{num}+{num1}={res}')
elif con=='-':
    res=num-num1
    print(f'{num}-{num1}={res}')
elif con=='*':
    res= num*num1
    print(f'{num}*{num1}={res}')
else:
    res=num/num1
    print(f'{num}/{num1}={res}')