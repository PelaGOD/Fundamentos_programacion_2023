matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

fila = len(matriz)
columna = len(matriz[0])

def cargar(mtz, f, c):
    for i in range(f):
        for j in range(c):
            mtz[i][j] = float(input(f'Ingrese número en la posición [{i}][{j}]: '))

def sumsucursal(mtz,f,c):
    sumS=0.0
    for i in range(f):
        for j in range(c):
            sumS=sumS+mtz[i-1][j-1]
    return sumS

def sumartic(mtz,f,c):
    sumA=0.0
    for j in range(f):
        for i in range(c):
            sumA=sumA+mtz[i][j]
    return sumA

cargar(matriz,fila,columna)
sumArticulo=sumartic(matriz,fila,columna)
sumSucursal=sumsucursal(matriz,fila,columna)
print(f'ventas por sucursal es de: ${sumSucursal} y ventas por articulos es de : ${sumArticulo}')

