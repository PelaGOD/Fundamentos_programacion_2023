matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
fila = len(matriz)
columna = len(matriz[0])

def cargar(mtz, f, c):
    for i in range(f):
        for j in range(c):
            mtz[i][j] = int(input(f'Ingrese número en la posición [{i}][{j}]: '))

def mayormtz(mtz, f, c):
    maxmtz = None
    for i in range(f):
        for j in range(c):
            if (i + j) % 2 == 0:
                if maxmtz is None or mtz[i][j] > maxmtz:
                    maxmtz = mtz[i][j]
    return maxmtz

cargar(matriz, fila, columna)
maximo = mayormtz(matriz, fila, columna)
print(f'El número mayor en las posiciones pares es: {maximo}')
