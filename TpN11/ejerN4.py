# 4- Escribir un programa que lea los valores de c/campo de un registro de stock de un almacén. Los # 
#        campos son:                                                                                # 
#            - Cod_art: integer;                                                                    # 
#            - Descripción: string [30];                                                            # 
#            - Cantidad: word; (0 ..65535)                                                          # 
#            - Precio_unitario: real;                                                               #   
#                Se pide además:                                                                    # 
#                    a- Cargar datos hasta que el cod_art = 0.                                      # 
#                    b- Mostrar del artículo más caro, cantidad en existencia.                      #  
#                    c- Dado un cod_articulo ver si existe.                                         # 
#                    d- Mostrar si este almacén vende queso “Don Bautista”.                         #  
#                    e- Mostrar el artículo con menor existencia.                                   # 
#                    f- Mostrar cual es el artículo más barato.                                     #


Articulos = [0, 0, 0, 0, 0, 0]
lim = len(Articulos)

def cargar_lista():
    cod_art = int(input('Codigo del Articulo: '))
    desc = str(input('Descripción del Articulo: '))
    cant = int(input('Cantidad del Articulo en Stock: '))
    precio_unit = int(input('Precio C/U: $'))

    datosArticulo = {'Cod_Art': cod_art, 'Desc': desc, 'Cant': cant,'Precio_Unit':precio_unit}
    return datosArticulo

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
                if v[j]['Cod_Art'] > v[j + 1]['Cod_Art']:
                    v[j], v[j + 1] = v[j + 1], v[j]

def ArticuloMayorP(v):
    articulo_mayor_p = None

    for i in range(lim):
        if articulo_mayor_p is None or (v[i] is not None and v[i]['Precio_Unit'] > articulo_mayor_p['Precio_Unit']):
            articulo_mayor_p = v[i]

    if articulo_mayor_p is not None:
        return print('La cantidad de articulos de mayor precio son :', articulo_mayor_p)
    else:
        return print('No hay articulos cargados.')
    
def Busq_Bianria(v,l):
    inicio = 0
    fin=l-1
    pos=0
    buscado=int(input('Ingrese buscado'))
    while inicio<=fin and pos==0:
        medio=(inicio+fin)//2
        if v[medio]['Desc'] == buscado:
            pos=medio
            return print(v[pos])
        elif v[medio]['Desc'] < buscado:
            inicio=medio+1
        elif v[medio]['Desc'] > buscado:
            fin = medio-1
    return print(f'el codigo: {buscado} no existe')

def Don_Bautista(v,l):
    inicio = 0
    fin=l-1
    pos=0
    buscado='Don Bautista'
    while inicio<=fin and pos==0:
        medio=(inicio+fin)//2
        if v[medio]['Cod_Art'] == buscado:
            pos=medio
            return print(f'Este almacen tiene {buscado}')
        elif v[medio]['Cod_Art'] < buscado:
            inicio=medio+1
        elif v[medio]['Cod_Art'] > buscado:
            fin = medio-1
    return print(f'el articulo: {buscado} no se encuentra en este almacen')

def Articulo_Menor_E(v):
    articulo_menor_e = None

    for i in range(lim):
        if articulo_menor_e is None or (v[i] is not None and v[i]['Cant'] < articulo_menor_e['Cant']):
            articulo_menor_e = v[i]

    if articulo_menor_e is not None:
        return print('La cantidad de articulos de mayor precio son :', articulo_menor_e)
    else:
        return print('No hay articulos cargados.')
    
def ArticuloMenorP(v):
    articulo_menor_p = None

    for i in range(lim):
        if articulo_menor_p is None or (v[i] is not None and v[i]['Precio_Unit'] > articulo_menor_p['Precio_Unit']):
            articulo_menor_p = v[i]

    if articulo_menor_p is not None:
        return print('La cantidad de articulos de mayor precio son :', articulo_menor_p)
    else:
        return print('No hay articulos cargados.')
    

cargar(Articulos)
bubble_sort(Articulos)
ArticuloMayorP(Articulos)
Busq_Bianria(Articulos,lim)
Don_Bautista(Articulos,lim)
Articulo_Menor_E(Articulos)
ArticuloMenorP(Articulos)