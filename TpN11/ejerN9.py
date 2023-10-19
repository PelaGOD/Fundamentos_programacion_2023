#       En una distribuidora se lleva mensualmente,                                                     #
#       la siguiente información:                                                                       #
#           código de producto                                                                          #
#           cantidad vendida                                                                            #
#           costo de fabricación del producto (por unidad)                                              #
#           precio unitario de venta al público.                                                        #
#               Se desea calcular:                                                                      #
#                   a- Cual fue el producto más vendido.                                                #
#                   b- Cual fue la ganancia que se obtuvo al vender dicho producto (en x cantidad).     #
#                   c- Cual es el costo unitario del producto más caro.                                 #

distribuidora = [0, 0, 0, 0, 0, 0]
lim = len(distribuidora)

def cargar_lista():
    cod_producto = int(input('Codigo de producto: '))
    ca_vendidas = int(input('Cantidad vendida: '))
    co_productouc = float(input('Costo de fabricacion del producto: $'))
    precio_ucp = float(input('Precio unitario de venta al publico: $'))

    datosDistribuidora = {'Cod_Producto': cod_producto, 'Ca_Vendidas': ca_vendidas, 'Co_ProductoUC': co_productouc,'Precio_UCP':precio_ucp}
    return datosDistribuidora

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
                if v[j]['Ca_Vendidas'] > v[j + 1]['Ca_Vendidas']:
                    v[j], v[j + 1] = v[j + 1], v[j]

def producto_mas_vendido(v):
    global lim 
    producto_m_v = None

    for i in range(lim):
        if producto_m_v is None or (v[i] is not None and v[i]['Ca_Vendidas'] > producto_m_v['Ca_Vendidas']):
            producto_m_v = v[i]

    if producto_m_v is not None:
        return print(f'el producto mas vendido es :{producto_m_v}')
    else:
        return print('No hay datos de empleado.')

def Busq_Bianria(v):
    global lim
    inicio = 0
    fin=lim-1
    pos=0
    buscado=int(input('Ingrese buscado'))
    while inicio<=fin and pos==0:
        medio=(inicio+fin)//2
        if v[medio]['Cod_Producto'] == buscado:
            pos=medio
            return print(v[pos])
        elif v[medio]['Cod_Producto'] < buscado:
            inicio=medio+1
        elif v[medio]['Cod_Producto'] > buscado:
            fin = medio-1
    return print(f'el codigo: {buscado} no existe')

def producto_mas_caro(v):
    global lim 
    producto_m_c = None

    for i in range(lim):
        if producto_m_c is None or (v[i] is not None and v[i]['Precio_UCP'] > producto_m_c['Precio_UCP']):
            producto_m_c = v[i]

    if producto_m_c is not None:
        return print(f'el producto mas vendido es :{producto_m_c}')
    else:
        return print('No hay datos de empleado.')
    

cargar(distribuidora)
bubble_sort(distribuidora)
producto_mas_vendido(distribuidora)
Busq_Bianria(distribuidora)
producto_mas_caro(distribuidora)