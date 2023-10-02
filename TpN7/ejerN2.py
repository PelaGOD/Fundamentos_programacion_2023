def cargar_vector(vec):
    lim = 0
    num = int(input('Ingrese un numero (o ingrese 0 para salir): '))
    while num != 0 and lim < len(vec):
        vec[lim] = num
        lim += 1
        if lim < len(vec):
            num = int(input('Ingrese un numero (o ingrese 0 para salir): '))
    return lim

def calculo(vec, lim):
    ac = 1
    for i in range(lim):
        ac = ac*vec[i]
    print(f'El producto de los números es igual a {ac}')

def mostrar_vector(vec, lim):
    for i in range(lim):
        print(vec[i])

vector = [0, 0, 0, 0, 0, 0, 0, 0]
limit = cargar_vector(vector)
mostrar_vector(vector, limit)
calculo(vector, limit)

