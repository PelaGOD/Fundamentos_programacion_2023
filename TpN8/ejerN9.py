# Una empresa de transporte de pasajeros de larga distancia posee micros de 4 categorías y viaja a 250 localidades de zonas turísticas del país
# Se dispone de un registro de todos los pasajes vendidos en una temporada consistente en: código de categoría (a, b, c, d) y código de destino (1 a 250)
# Se dispone también de un listado ordenado por código del nombre de cada localidad de destino

# Ejemplo de registro de pasajes vendidos
registro = [("a", 10), ("b", 15), ("c", 20), ("a", 10), ("d", 25), ("b", 15), ("c", 20), ("d", 25), ("a", 30), ("b", 35), ("c", 40), ("d", 45)]

# Ejemplo de listado de nombres de localidades
nombres = ["Bariloche", "Córdoba", "Mendoza", "Salta", "Rosario", "Mar del Plata", "Ushuaia", "Iguazú", "Tucumán", "La Rioja"]

# a- Se pide informar la cantidad de pasajeros por localidad, por categoría

# Crear una matriz vacía de 250 filas (localidades) y 4 columnas (categorías)
matriz = [[0 for j in range(4)] for i in range(250)]

# Recorrer el registro y sumar los pasajeros a la matriz según el código de destino y la categoría
for categoria, destino in registro:
    # Restar uno a los índices para que coincidan con la matriz
    i = destino - 1
    j = ord(categoria) - ord("a")

    # Sumar los pasajeros a la posición correspondiente de la matriz
    matriz[i][j] += 1

# Informar la cantidad de pasajeros por localidad, por categoría
print("La cantidad de pasajeros por localidad, por categoría es:")
for i in range(len(matriz)):
    # Si la fila tiene algún valor distinto de cero, significa que hay pasajeros para esa localidad
    if any(matriz[i]):
        # Obtener el nombre de la localidad según el índice
        nombre = nombres[i]

        # Mostrar el nombre y los pasajeros por categoría
        print(f"{nombre}: {matriz[i][0]} pasajeros en categoría a, {matriz[i][1]} pasajeros en categoría b, {matriz[i][2]} pasajeros en categoría c, {matriz[i][3]} pasajeros en categoría d")

# b- Informar la cantidad de pasajeros por localidad

# Crear una lista vacía de 250 elementos para almacenar la cantidad de pasajeros por localidad
lista = [0 for i in range(250)]

# Recorrer el registro y sumar los pasajeros a la lista según el código de destino
for categoria, destino in registro:
    # Restar uno al índice para que coincida con la lista
    i = destino - 1

    # Sumar uno al elemento correspondiente de la lista
    lista[i] += 1

# Informar la cantidad de pasajeros por localidad
print("La cantidad de pasajeros por localidad es:")
for i in range(len(lista)):
    # Si el elemento es distinto de cero, significa que hay pasajeros para esa localidad
    if lista[i]:
        # Obtener el nombre de la localidad según el índice
        nombre = nombres[i]

        # Mostrar el nombre y los pasajeros
        print(f"{nombre}: {lista[i]} pasajeros")

# c- Informar la cantidad de pasajeros por categoría

# Crear una lista vacía de 4 elementos para almacenar la cantidad de pasajeros por categoría
lista = [0 for j in range(4)]

# Recorrer el registro y sumar los pasajeros a la lista según el código de categoría
for categoria, destino in registro:
    # Restar uno al índice para que coincida con la lista
    j = ord(categoria) - ord("a")

    # Sumar uno al elemento correspondiente de la lista
    lista[j] += 1

# Informar la cantidad de pasajeros por categoría
print("La cantidad de pasajeros por categoría es:")
for j in range(len(lista)):
    # Obtener el nombre de la categoría según el índice
    categoria = chr(j + ord("a"))

    # Mostrar el nombre y los pasajeros
    print(f"{categoria}: {lista[j]} pasajeros")

# d- Informar el nombre de la localidad a la que viajó la mayor cantidad de pasajeros

# Crear una variable para almacenar el máximo de pasajeros
maximo = 0

# Crear una variable para almacenar el índice del máximo
indice = 0

# Recorrer la lista de pasajeros por localidad y buscar el máximo y su índice
for i in range(len(lista)):
    # Si el elemento es mayor que el máximo, actualizar el máximo y el índice
    if lista[i] > maximo:
        maximo = lista[i]
        indice = i

# Obtener el nombre de la localidad según el índice
nombre = nombres[indice]

# Informar el nombre de la localidad con más pasajeros
print(f"La localidad a la que viajó la mayor cantidad de pasajeros es: {nombre}")

# e- Informar el nombre de la localidad a la que viajó la menor cantidad de pasajeros

# Crear una variable para almacenar el mínimo de pasajeros
minimo = maximo

# Crear una variable para almacenar el índice del mínimo
indice = 0

# Recorrer la lista de pasajeros por localidad y buscar el mínimo y su índice
for i in range(len(lista)):
    # Si el elemento es menor que el mínimo y distinto de cero, actualizar el mínimo y el índice
    if lista[i] < minimo and lista[i] != 0:
        minimo = lista[i]
        indice = i

# Obtener el nombre de la localidad según el índice
nombre = nombres[indice]

# Informar el nombre de la localidad con menos pasajeros
print(f"La localidad a la que viajó la menor cantidad de pasajeros es: {nombre}")
