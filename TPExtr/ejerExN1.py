montoM= float(input('Ingrese monto maximo: $'))
sueldo=float(input('Ingrese sueldo: $'))
c=0
while montoM>sueldo:
    montoM=montoM-sueldo
    sueldo=float(input('ingrese sueldo a pagar'))
    c+=1
    print('sueldo pagado:$')

print(f'sueldos pagados ${c}')