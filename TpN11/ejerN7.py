#   En una empresa se guardan:                                  #
#       -los códigos de empleados                               #
#       -edades                                                 #
#       -los sueldos                                            #
#       -la antigüedad en años (Nº entero)                      #
#           Se pide calcular:                                   #
#               a- Sueldo del empleado más antiguo y edad.      #
#               b- Sueldo del empleado más nuevo y edad.        #
#               c- Promedio de sueldos.                         #
#               d- Promedio de edades.                          # 

cantidad_Empleados = [0, 0, 0, 0, 0, 0]
lim = len(cantidad_Empleados)

def cargar_lista():
    cod_emp = int(input('Ingrese Codigo de Empleado: '))
    edad = int(input('Ingrese edad: '))
    sueldo = float(input('Ingrese sueldo: $'))
    años_anti = int(input('Ingrese años de antiguedad: '))

    datosEmpleado = {'Cod_Emp': cod_emp, 'Edad': edad, 'Sueldo': sueldo, 'Años_Anti':años_anti}
    return datosEmpleado

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
                if v[j]['Cod_Emp'] > v[j + 1]['Cod_Emp']:
                    v[j], v[j + 1] = v[j + 1], v[j]

def Sueldo_Empleado_Mayor(v):
    sueldo_empleado_mayor = None

    for i in range(lim):
        if sueldo_empleado_mayor is None or (v[i] is not None and v[i]['Años_Anti'] > sueldo_empleado_mayor['Años_Anti']):
            sueldo_empleado_mayor = v[i]

    if sueldo_empleado_mayor is not None:
        return print(sueldo_empleado_mayor)
    else:
        return print('No hay datos de empleado.')

def Sueldo_Empleado_Menor(v):
    sueldo_empleado_menor = None

    for i in range(lim):
        if sueldo_empleado_menor is None or (v[i] is not None and v[i]['Años_Anti'] < sueldo_empleado_menor['Años_Anti']):
            sueldo_empleado_menor = v[i]

    if sueldo_empleado_menor is not None:
        return print(sueldo_empleado_menor)
    else:
        return print('No hay datos de empleado.')

def Promedio_sueldo(v,l):
    sum_sueldo=0
    prom_sueldo=float
    for i in range(0,l):
        sum_sueldo = sum_sueldo+v[i]['Sueldo']
    prom_sueldo= sum_sueldo/l
    return print(f'El promedio de sueldo es de : %{prom_sueldo}')

def Promedio_edad(v,l):
    sum_edad=0
    prom_edad=float
    for i in range(0,l):
        sum_edad = sum_edad+v[i]['Edad']
    prom_edad= sum_edad/l
    return print(f'El promedio de sueldo es de : %{prom_edad}')


cargar(cantidad_Empleados)
bubble_sort(cantidad_Empleados)
Sueldo_Empleado_Mayor(cantidad_Empleados)
Sueldo_Empleado_Menor(cantidad_Empleados)
Promedio_sueldo(cantidad_Empleados,lim)
Promedio_edad(cantidad_Empleados,lim)