PIni = float(input('Indique el precio del articulo inicial: $'))
PFin = float(input('Indique el precio del articulo a fin de año: $'))

porc = (PFin*100/PIni)-100

print(f'El porcentaje de aumento es de : %{porc}')