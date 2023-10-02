# Sumar los elementos que están en la diagonal principal de una matriz dada
def sumar_diagonal(matriz):
    # Crear una variable para almacenar la suma
    suma = 0

    # Recorrer la matriz por filas y columnas
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            # Si el índice de la fila es igual al de la columna, el elemento está en la diagonal principal
            if i == j:
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

# Mostrar la suma de los elementos en la diagonal principal
suma = sumar_diagonal(matriz)
print("La suma de los elementos en la diagonal principal es:")
print(suma)
