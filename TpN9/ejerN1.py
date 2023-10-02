"Hacer un algoritmo que:"
"- Lea una lista de números de teclado que culmina con uno negativo."
"- Los ordene en forma creciente y Visualice la lista ordenada."
"- Buscar si existe el Nº 27 en la lista."

def cargarVector(vect):
    lim = 0
    num = int(input('Ingrese un numero (o ingrese 0 para salir): '))
    while num >0 and lim < len(vect):
        vect[lim] = num
        lim += 1
        if lim < len(vect):
            num = int(input('Ingrese un numero (o ingrese 0 para salir): '))
    return lim

def ord_burbuja(vect,lim):
    n = lim

    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            if vect[j] > vect[j+1]:
                vect[j], vect[j+1] = vect[j+1], vect[j]
    return vect

def Busq_Bianria(vect,lim):
    inicio = 0
    fin=lim-1
    pos=0
    buscado=int(input('Ingrese buscado'))
    while inicio<=fin and pos==0:
        medio=(inicio+fin)//2
        if vect[medio] == buscado:
            pos=medio
            return print(f'el buscado esta {buscado}')
        elif vect[medio] < buscado:
            inicio=medio+1
        elif vect[medio] > buscado:
            fin = medio-1
    return print(f'el buscado {buscado} no esta')


vector= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

cargarVector(vector)
ord_burbuja(vector,len(vector))
Busq_Bianria(vector,len(vector))
