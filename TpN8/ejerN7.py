# Sumar los elementos que están por encima de la diagonal principal de una matriz dada
def sumar_diagonal(matriz):
    # Crear una variable para almacenar la suma
    suma = 0

    # Recorrer la matriz por filas y columnas
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            # Si el índice de la columna es mayor que el de la fila, el elemento está por encima de la diagonal principal
            if j > i:
                # Sumar el elemento a la suma
                suma += matriz[i][j]
    
    # Devolver la suma
    return suma

# Ejemplo de una matriz dada
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Mostrar la matriz
print("La matriz es:")
for fila in matriz:
    print(fila)

# Mostrar la suma de los elementos por encima de la diagonal principal
suma = sumar_diagonal(matriz)
print("La suma de los elementos por encima de la diagonal principal es:")
print(suma)
