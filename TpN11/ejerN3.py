#3- Se tiene una clase de 30 estudiantes, para c/u se almacenan los siguientes datos:  #
#    - Nro_estudiante                                                                  #
#    - Nombre                                                                          #
#    - Nota                                                                            #
#        Se pide:                                                                      #
#        a- Lista de alumnos con sus respectivas notas ordenados alfabéticamente.      # 
#        b- Nro. de estudiante con mayor nota.                                         #
#        c- Nombre de estudiante de menor nota.                                        # 
#        d- Nota que obtuvo la alumna Laura Suárez.                                    #

cantidad_Estudiantes = [0, 0, 0, 0, 0, 0]
lim = len(cantidad_Estudiantes)

def cargar_lista():
    num_est = int(input('Ingrese número del estudiante: '))
    nombre = str(input('Ingrese nombre completo del estudiante: '))
    nota = float(input('Ingrese la nota del estudiante: '))

    datosEstudiante = {'NEst': num_est, 'NombreC': nombre, 'Nota': nota}
    return datosEstudiante

def cargar(v):
    global lim
    resp = input('¿Quiere cargar datos? (si o no): ')
    while resp == 'si' and lim < len(v):
        v[lim] = cargar_lista()
        lim += 1
        if lim < len(v):
            resp = input('¿Quiere cargar otro? (si o no): ')

def bubble_sort(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if v[j] is not None and v[j + 1] is not None:
                if v[j]['NombreC'] > v[j + 1]['NombreC']:
                    v[j], v[j + 1] = v[j + 1], v[j]

def EstudianteMayorNota(v):
    alumno_mayor_nota = None

    for i in range(lim):
        if alumno_mayor_nota is None or (v[i] is not None and v[i]['Nota'] > alumno_mayor_nota['Nota']):
            alumno_mayor_nota = v[i]

    if alumno_mayor_nota is not None:
        return print('El alumno con mayor nota:', alumno_mayor_nota)
    else:
        return print('No hay estudiantes cargados.')

def EstudianteMenorNota(v):
    alumno_menor_nota = None

    for i in range(lim):
        if alumno_menor_nota is None or (v[i] is not None and v[i]['Nota'] < alumno_menor_nota['Nota']):
            alumno_menor_nota = v[i]

    if alumno_menor_nota is not None:
        return print('El alumno con menor nota:', alumno_menor_nota)
    else:
        return print('No hay estudiantes cargados.')

def encontrar_alumno_por_nombre(v):
    nombre_buscado = 'Laura Suarez'
    for i in range(lim):
        if v[i] is not None and v[i]['NombreC'] == nombre_buscado:
            return v[i]
        else:
            return None  # Retorna None si el nombre no se encuentra

cargar(cantidad_Estudiantes)
bubble_sort(cantidad_Estudiantes)
EstudianteMayorNota(cantidad_Estudiantes)
EstudianteMenorNota(cantidad_Estudiantes)

alumno_encontrado = encontrar_alumno_por_nombre(cantidad_Estudiantes)
nombre_buscado = 'Laura Suarez'

if alumno_encontrado is not None:
    print(f"Se encontró a {nombre_buscado} en la lista de alumnos.")
    print("Nota:", alumno_encontrado['Nota'])
else:
    print(f"{nombre_buscado} no se encuentra en la lista de alumnos.")

