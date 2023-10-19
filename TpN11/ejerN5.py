#   En una librería se almacenan los datos de x cantidad de libros,                     #
#   por cada libro se tiene la siguiente información:                                   #
#       código y stock.                                                                 #
#       Realizar un programa que informe cuando se deba reponer stock de cada libro,    #
#           considerando stock mínimo = 3 libros.                                       # 



libreria = [0, 0, 0, 0, 0, 0]
lim = len(libreria)

def cargar_lista():
    nombre = str(input('Ingrese Nombre del Libro: '))
    codigo = int(input('Ingrese Codigo de Libro: '))
    stock = int(input('Ingrese Stock: '))

    datosLibreria = {'Nombre': nombre, 'Codigo': codigo, 'Stock': stock}
    return datosLibreria

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
                if v[j]['Stock'] > v[j + 1]['Stock']:
                    v[j], v[j + 1] = v[j + 1], v[j]

def stock_menos_3(v):
    global lim
    for i in range(0,lim-1):
        if v[i]['Stock']<3:
            print(v[i])
            print('Necesita ser reabastecido')


cargar(libreria)
bubble_sort(libreria)
stock_menos_3(libreria)
