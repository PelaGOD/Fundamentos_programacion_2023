# Dada una matriz de 5 filas y 10 columnas
matriz = [[0 for j in range(10)] for i in range(5)]

# a- Escribir el algoritmo necesario para cargar la matriz con valores
def cargar_matriz(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = float(input(f"Ingrese el valor de la posición [{i}][{j}]: "))

# b- Determinar la sumatoria de c/u de las columnas
def sumar_columnas(m):
    suma = [0 for j in range(len(m[0]))]
    for i in range(len(m)):
        for j in range(len(m[i])):
            suma[j] += m[i][j]
    return suma

# c- Mostrar el mayor valor de c/u de sus columnas
def mayor_columnas(m):
    mayor = [m[0][j] for j in range(len(m[0]))]
    for i in range(1, len(m)):
        for j in range(len(m[i])):
            if m[i][j] > mayor[j]:
                mayor[j] = m[i][j]
    return mayor

# d- Mostrar la posición (F,C) del menor valor de la matriz
def menor_matriz(m):
    menor = m[0][0]
    fila = 0
    columna = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] < menor:
                menor = m[i][j]
                fila = i
                columna = j
    return (fila, columna)

# Cargar la matriz con valores ingresados por el usuario
cargar_matriz(matriz)

# Mostrar la matriz
print("La matriz es:")
for fila in matriz:
    print(fila)

# Mostrar la sumatoria de cada columna
suma = sumar_columnas(matriz)
print("La sumatoria de cada columna es:")
print(suma)

# Mostrar el mayor valor de cada columna
mayor = mayor_columnas(matriz)
print("El mayor valor de cada columna es:")
print(mayor)

# Mostrar la posición del menor valor de la matriz
menor = menor_matriz(matriz)
print("La posición del menor valor de la matriz es:")
print(menor)
