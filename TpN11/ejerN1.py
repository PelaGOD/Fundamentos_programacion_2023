# Un arreglo de registros contiene la descripción de personas a efectos estadísticos, Cada registro tiene los campos:   #
#    nombre,                                                                                                            #
#    edad,                                                                                                              #
#    peso,                                                                                                              #
#    sexo,                                                                                                              #
#    altura,                                                                                                            #
#    color de piel,                                                                                                     #
#    color de ojos                                                                                                      #
#    nacionalidad.                                                                                                      #
#        Se pide:                                                                                                       #
#            - Cantidad de personas con más de sesenta años.                                                            #
#            - Cantidad de mujeres de más de 1,70m.                                                                     #
#            - Porcentaje de personas con menos de 50Kg. de peso.                                                       #
#            - % de hombres de origen cubano.                                                                           #
#            - % de mujeres argentinas.                                                                                 #
#            - % de personas con menos de 30 años y ojos violetas.                                                      #

Registro = [0, 0, 0, 0, 0, 0]
lim = len(Registro)

def cargar_lista():
    nomap = str(input('Ingrese Nombre y apellido: '))
    edad = int(input('Ingrese edad: '))
    peso = float(input('Ingrese peso: '))
    sexo = str(input('Ingrese su sexo (Femenino/Masculino): '))
    altura = float(input('Ingrese altura: '))
    cpiel = str(input('Ingrese Color de piel: '))
    cojos = str(input('Ingrese Color de ojos: '))
    nacio = str(input('Ingrese su nacional: '))

    datosAlumno = {'NomAp':nomap,'Edad':edad,'Peso':peso,'Sexo':sexo,'Altura':altura,'CPiel':cpiel,'COjos':cojos,'Nacio':nacio}
    return datosAlumno

def cargar(v):
    limt=int
    global lim
    resp = input('¿Quiere cargar datos? (si o no): ')
    while resp == 'si' and lim < len(v):
        v[lim] = cargar_lista()
        lim += 1
        if lim < len(v):
            resp = input('¿Quiere cargar otro? (si o no): ')
    limt=lim
    return limt

def bubble_sort_e(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if v[j] is not None and v[j + 1] is not None:
                if v[j]['Edad'] < v[j + 1]['Edad']:
                    v[j], v[j + 1] = v[j + 1], v[j]


def mayor60(v,l):
    for i in range(0,l-1):
        if v[i]['Edad'] >60:
            ContM60 += 1
    
    return ContM60

def porc_menos30_violetas(v,l):
    for i in range(0,l-1):
        if v[i]['Edad'] <30 and v[i]['COjos']:
            ContM30 += 1
    Porcm30v=(l*ContM30)/100
    return 
def bubble_sort_a(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if v[j] is not None and v[j + 1] is not None:
                if v[j]['Edad'] < v[j + 1]['Edad']:
                    v[j], v[j + 1] = v[j + 1], v[j]

def mayor170(v,l):
    for i in range(0,l-1):
        if v[i]['Altura'] >1.70 and v[i]['Sexo']=='Femenino':
            ContM170 += 1
    
    return ContM170

def bubble_sort_p(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if v[j] is not None and v[j + 1] is not None:
                if v[j]['Peso'] > v[j + 1]['Peso']:
                    v[j], v[j + 1] = v[j + 1], v[j]

def pesomenor50(v,l):
    for i in range(0,l-1):
        if v[i]['Peso'] <=50:
            Cont50 += 1
    por50kg=(l*Cont50)/100
    return por50kg

def bubble_sort_n(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if v[j] is not None and v[j + 1] is not None:
                if v[j]['Nacio'] < v[j + 1]['Nacio']:
                    v[j], v[j + 1] = v[j + 1], v[j]

def porc_hom_cuba(v,l):
    for i in range(0,l-1):
        if v[i]['Nacio']=='Cubano' and v[i]['Sexo']=='Masculino':
            contCM +=1

    porcCM=(l*contCM)/100
    return porcCM

def porc_muj_arg(v,l):
    for i in range(0,l-1):
        if v[i]['Nacio']=='Argentina' and v[i]['Sexo']=='Femenino':
            contMA +=1

    porcMA=(l*contMA)/100
    return porcMA


lim=cargar(Registro)
bubble_sort_e(Registro)
may60=mayor60(Registro,lim)
print(f'La cantidad de personas mayores de 60 es de: {may60}')
porcm30=porc_menos30_violetas(Registro,lim)
print(f'el porcentaje de personas menores de 30 con ojos violeta es de: {porcm30}%')
bubble_sort_a(Registro)
altm170=mayor170(Registro,lim)
print(f'Cantidad de mujeres que miden mas de 1.70m es de: {altm170}')
bubble_sort_p(Registro)
peso50=pesomenor50(Registro,lim)
print(f'el porcentaje de personas que pesan menos de 50kg es de: {peso50}%')
bubble_sort_n(Registro)
porchc=porc_hom_cuba(Registro,lim)
print(f'el porcentaje de hombres cubanos es de: {porchc}%')
porcma= porc_muj_arg(Registro,lim)
print(f'el porcentaje de mujeres argentinas es de: {porcma}%')