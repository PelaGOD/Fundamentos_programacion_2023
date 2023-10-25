# Supongamos que definimos un arreglo de 1000 pólizas de seguro de vida, cada una posee                             #
#     Nº de póliza                                                                                                  #
#     nombre del asegurado                                                                                          #
#     dirección                                                                                                     #
#     año de nacimiento                                                                                             #
#     cantidad asegurada                                                                                            #
#     cuota                                                                                                         #
#         Codificar un algoritmo que permita ingresar pólizas en la estructura anterior.                            #
#         Además, se pide:                                                                                          #
#             - Mostrar los nombre y direcciones de las personas que cumplen 70 años en el corriente año.           #
#             - Mostrar las personas cuya cuota es menor a $ 30.00.                                                 #
#             - Mostrar las personas que tengan asegurada un monto mayor a $100.000 ordenados alfabéticamente       #
#             - Mostrar si Pedro Fernández está asegurado en la compañía.                                           #

# Definir una estructura de datos para las pólizas de seguro de vida
polizas = [None] * 1000  # Crear una lista con 1000 elementos inicialmente vacíos

# Función para cargar los datos de una póliza
def cargar_poliza():
    numero_poliza = int(input('Ingrese el número de póliza: '))
    nombre_asegurado = input('Ingrese el nombre del asegurado: ')
    direccion = input('Ingrese la dirección: ')
    ano_nacimiento = int(input('Ingrese el año de nacimiento: '))
    cantidad_asegurada = float(input('Ingrese la cantidad asegurada: '))
    cuota = float(input('Ingrese la cuota: '))
    
    poliza = {
        'Número de póliza': numero_poliza,
        'Nombre del asegurado': nombre_asegurado,
        'Dirección': direccion,
        'Año de nacimiento': ano_nacimiento,
        'Cantidad asegurada': cantidad_asegurada,
        'Cuota': cuota
    }
    
    return poliza

# Función para verificar si una persona cumple 70 años este año
def cumple_70(p):
    ano_actual = 2023  # Supongamos que el año actual es 2023
    return ano_actual - p['Año de nacimiento'] == 70

# Función para mostrar personas con cuota menor a $30
def cuota_menor_a_30(p):
    return p['Cuota'] < 30.00

# Cargar las pólizas de seguro
posicion = 0  # Para rastrear la posición actual en la lista
continuar_carga = 'si'

while continuar_carga.lower() == 'si' and posicion < 1000:
    poliza = cargar_poliza()
    polizas[posicion] = poliza
    posicion += 1
    continuar_carga = input('¿Desea cargar otra póliza? (si o no): ')

# Mostrar los nombre y direcciones de las personas que cumplen 70 años este año
print('Personas que cumplen 70 años este año:')
for poliza in polizas:
    if poliza and cumple_70(poliza):
        print(f'Nombre: {poliza["Nombre del asegurado"]}, Dirección: {poliza["Dirección"]}')

# Mostrar las personas con cuota menor a $30
print('\nPersonas con cuota menor a $30.00:')
for poliza in polizas:
    if poliza and cuota_menor_a_30(poliza):
        print(f'Nombre: {poliza["Nombre del asegurado"]}')

