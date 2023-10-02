monto=float(input('Ingrese el precio: $'))

print(f'Precio : ${monto}')
if monto >= 1000:
    monto=(monto*0.10)-monto
    print(f'precio con descuento 10%: ${monto}')
else:
    monto=monto-(monto*0.02)
    print(f'precio con descuento 2%: ${monto}')