#Calcular la media de una lista de 25 estudiantes de una clase de informática con notas en cuatro materias#

notEstud = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
fila = len(notEstud)
columna = len(notEstud[0])

def cargarNot(estudN, f, c):
    for i in range(f):
        for j in range(c):
            estudN[i][j] = int(input(f'Ingrese la nota para el estudiante {i+1}, materia {j+1}: '))

def PromNotEst(estudN, f, c):
    for i in range(f):
        resultado = 0  # Initialize resultado to 0 for each student
        for j in range(c):
            resultado += estudN[i][j]
        prom = resultado / c  # Calculate the average for each student
        print(f'El promedio del estudiante {i+1} es: {prom}')

cargarNot(notEstud, fila, columna)
PromNotEst(notEstud, fila, columna)
