def carga_vector(vec):
    lim = 0
    num = int(input('Ingrese un numero (o ingrese 0 para salir): '))
    while num != 0 and lim < len(vec):
        vec[lim] = num
        lim += 1
        if lim < len(vec):
            num = int(input('Ingrese un numero (o ingrese 0 para salir): '))
    return lim

def calculo(vec, lim):
    ac = 0
    for i in range(lim):
        rest = i % 2
        if rest != 0:
            ac = ac+vec[i]
    print(f'La suma de los números es igual a {ac}')

vector= [0,0,0,0,0,0,0,0,0,0]
limit=carga_vector(vector)

calculo(vector,limit)