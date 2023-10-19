#   De cada alumno de una materia ‘x’ se registra:          #
#       Nº de alumno                                        #
#       nota                                                #
#       sexo                                                #
#           Se desea saber:                                 #
#               a- cuantos varones aprobaron (nota>=4)      #
#               b- que % de mujeres sacó 10,                #
#               c- % de desaprobados.                       # 


alumnos = [0, 0, 0, 0, 0, 0]
lim = len(alumnos)

def cargar_lista():
    nalumno = int(input('Ingrese Codigo de Empleado: '))
    nota = float(input('Ingrese edad: '))
    sexo = str(input('Ingrese sexo: '))

    datosAlumno = {'NAlumno': nalumno, 'Nota': nota, 'Sexo': sexo}
    return datosAlumno

def cargar(v):
    global lim
    lim=0
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
                if v[j]['Nota'] > v[j + 1]['Nota']:
                    v[j], v[j + 1] = v[j + 1], v[j]

def nota_mayor_4_v(v):
    global lim
    for i in range(0,lim-1):
        if v[i]['Sexo'] =='Masculino' and v[i]['Nota'] >= 4:
            ContM += 1
    
    return ContM

def prom_mujere_10(v):
    global lim
    for i in range(0,lim-1):
        if v[i]['Sexo'] =='Femenino' and v[i]['Nota'] == 10:
            ContM += 1
    promm10 = ContM/lim
    
    return promm10

def prom_desaprobado(v):
    global lim
    for i in range(0,lim-1):
        if v[i]['Nota'] < 4:
            ContM += 1
    promd = ContM/lim
    
    return promd


cargar(alumnos)
bubble_sort(alumnos)
nota4v=(nota_mayor_4_v(alumnos))
print(f'La cantidad de alumons varones con nota mayor a 4 es de: {nota4v}')
prom10m=(prom_mujere_10(alumnos))
print(f'La promedio de alumnas aprobadas con nota 10 es de: %{prom10m}')
promdes=(prom_desaprobado(alumnos))
print(f'El promedio de alumnos desaprobados es de: %{promdes}')