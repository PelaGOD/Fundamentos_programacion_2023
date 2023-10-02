# Leer el vector de 10 elementos
vector = [float(input(f"Ingrese el elemento {i + 1}: ")) for i in range(10)]

# Comprobar las condiciones y emitir las leyendas correspondientes
positivas = True
negativas = True
cero = False

for elemento in vector:
    if elemento > 0:
        negativas = False
        cero = False
    elif elemento < 0:
        positivas = False
        cero = False
    else:
        positivas = False
        negativas = False
        cero = True

# Emitir las leyendas
if positivas:
    print("El vector tiene todas sus componentes positivas")
elif negativas:
    print("El vector tiene componentes negativas")
elif cero:
    print("El vector tiene algún cero")
else:
    print("El vector tiene componentes positivas y negativas")
