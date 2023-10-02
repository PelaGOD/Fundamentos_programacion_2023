matriz = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
fila = len(matriz)
columna = len(matriz[0])

def cargar(mtz, f, c):
    for i in range(f):
        for j in range(c):
            mtz[i][j] = int(input(f'Ingrese número en la posición [{i}][{j}]: '))
            if i == 3 and j == 5:
                print(f'El usuario {i} en el mes {j} pagó: ${mtz[i][j]}')

def mayorAporte(mtz, f, c):
    for j in range(c):
        mayorM = 0
        cli = 0
        for i in range(f):
            if mtz[i][j] > mayorM:
                mayorM = mtz[i][j]
                cli = i
        print(f'En el mes {j}, el cliente {cli} fue el que más aportó con: ${mayorM}')

def mayorT(mtz, f, c):
    MT = 0
    cli = 0
    for i in range(f):
        for j in range(c):
            if mtz[i][j] > MT:
                MT = mtz[i][j]
                cli = i
    
    print(f'El cliente {cli} fue el que más aportó en total con: ${MT}')

def MenorT(mtz, f, c):
    mes = 0
    MenT = float('inf')
    for j in range(c):
        total_mes = sum(mtz[i][j] for i in range(f))
        if total_mes < MenT:
            MenT = total_mes
            mes = j

    print(f'El mes en el que se recaudó menos es el mes {mes}')

cargar(matriz, fila, columna)
mayorAporte(matriz, fila, columna)
mayorT(matriz, fila, columna)
MenorT(matriz, fila, columna)
