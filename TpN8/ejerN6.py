# Se tiene un listado con los siguientes datos: Número de alumno (1 a n ) , número de materia (1 a m ), nota ( 0 a 10 )
# El listado se representa como una lista de tuplas de la forma (alumno, materia, nota)
listado = [(1, 1, 8), (2, 2, 7), (3, 3, 9), (1, 2, 6), (2, 3, 8), (3, 1, 7), (1, 3, 10), (2, 1, 5), (3, 2, 6)]

# Se asume que n y m son los valores máximos de alumno y materia en el listado
n = max(alumno for alumno, materia, nota in listado)
m = max(materia for alumno, materia, nota in listado)

# a- Crear una estructura bidimensional que almacene el promedio por materia de cada alumno e informarla asignándole en la impresión un guión en caso de faltar datos
def crear_matriz_promedio(listado, n, m):
    # Crear una matriz de n x m con ceros
    matriz = [[0 for j in range(m)] for i in range(n)]

    # Crear un diccionario que almacene la cantidad de notas por alumno y materia
    contador = {}

    # Recorrer el listado y sumar las notas a la matriz y al contador
    for alumno, materia, nota in listado:
        # Restar uno a los índices para que coincidan con la matriz
        i = alumno - 1
        j = materia - 1

        # Sumar la nota a la posición correspondiente de la matriz
        matriz[i][j] += nota

        # Sumar uno al contador de la posición correspondiente del diccionario
        contador[(i,j)] = contador.get((i,j), 0) + 1
    
    # Recorrer la matriz y dividir cada elemento por el contador correspondiente para obtener el promedio
    for i in range(n):
        for j in range(m):
            # Si el contador tiene un valor para la posición (i,j), dividir la matriz por ese valor
            if (i,j) in contador:
                matriz[i][j] /= contador[(i,j)]
            # Si no, asignar None a la matriz para indicar que falta el dato
            else:
                matriz[i][j] = None
    
    # Devolver la matriz con los promedios
    return matriz

# Informar la matriz con los promedios por materia de cada alumno
matriz_promedio = crear_matriz_promedio(listado, n, m)
print("La matriz con los promedios por materia de cada alumno es:")
for i in range(n):
    for j in range(m):
        # Si la matriz tiene un valor numérico en la posición (i,j), mostrarlo con dos decimales
        if isinstance(matriz_promedio[i][j], float):
            print(f"{matriz_promedio[i][j]:.2f}", end=" ")
        # Si no, mostrar un guión para indicar que falta el dato
        else:
            print("-", end=" ")
    print()

# b- Informar el porcentaje de alumnos que cursó cada materia y el promedio general por materia considerando los alumnos que la cursaron
def informar_porcentaje_y_promedio(matriz_promedio, n):
    # Crear una lista para almacenar el promedio general por materia
    promedio_general = [0 for j in range(len(matriz_promedio[0]))]

    # Crear una lista para almacenar el porcentaje de alumnos que cursó cada materia
    porcentaje = [0 for j in range(len(matriz_promedio[0]))]

    # Recorrer la matriz y sumar los valores a las listas
    for i in range(len(matriz_promedio)):
        for j in range(len(matriz_promedio[i])):
            # Si la matriz tiene un valor numérico en la posición (i,j), sumarlo al promedio general y al porcentaje
            if isinstance(matriz_promedio[i][j], float):
                promedio_general[j] += matriz_promedio[i][j]
                porcentaje[j] += 1
    
    # Recorrer las listas y dividir cada elemento por el número de alumnos para obtener el promedio y el porcentaje
    for j in range(len(promedio_general)):
        promedio_general[j] /= n
        porcentaje[j] /= n
    
    # Informar el porcentaje y el promedio general por materia
    print("El porcentaje de alumnos que cursó cada materia y el promedio general por materia son:")
    for j in range(len(promedio_general)):
        print(f"Materia {j+1}: {porcentaje[j]*100:.2f}% de alumnos, {promedio_general[j]:.2f} de promedio")

# Informar el porcentaje y el promedio general por materia
informar_porcentaje_y_promedio(matriz_promedio, n)

# c- Informar la cantidad de materias que cursó cada alumno y el promedio que obtuvo considerando las materias que cursó
def informar_cantidad_y_promedio(matriz_promedio):
    # Crear una lista para almacenar la cantidad de materias que cursó cada alumno
    cantidad = [0 for i in range(len(matriz_promedio))]

    # Crear una lista para almacenar el promedio que obtuvo cada alumno considerando las materias que cursó
    promedio = [0 for i in range(len(matriz_promedio))]

    # Recorrer la matriz y sumar los valores a las listas
    for i in range(len(matriz_promedio)):
        for j in range(len(matriz_promedio[i])):
            # Si la matriz tiene un valor numérico en la posición (i,j), sumarlo a la cantidad y al promedio
            if isinstance(matriz_promedio[i][j], float):
                cantidad[i] += 1
                promedio[i] += matriz_promedio[i][j]
    
    # Recorrer las listas y dividir cada elemento del promedio por la cantidad correspondiente para obtener el promedio
    for i in range(len(promedio)):
        promedio[i] /= cantidad[i]
    
    # Informar la cantidad y el promedio por alumno
    print("La cantidad de materias que cursó cada alumno y el promedio que obtuvo son:")
    for i in range(len(cantidad)):
        print(f"Alumno {i+1}: {cantidad[i]} materias, {promedio[i]:.2f} de promedio")

# Informar la cantidad y el promedio por alumno
informar_cantidad_y_promedio(matriz_promedio)