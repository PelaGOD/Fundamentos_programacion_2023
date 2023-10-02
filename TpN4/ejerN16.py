mes =int(input('ingrese el mes (1/12): '))

if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
    print(f'el mes {mes} tiene 31 dias')
elif mes==4 or mes==6 or mes==9 or mes==11:
    print(f'el mes {mes} tiene 30 dias')
else:
    print(f'el mes {mes} tiene 28 o 29 dias')
