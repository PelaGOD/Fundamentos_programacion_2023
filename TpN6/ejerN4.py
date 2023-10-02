def mostrar(nom,edad):
    print(f'nombre y apellido:{nom}')
    print(f'edad:{edad}')

nomyap=str(input('ingrese nombre y apellido:'))
while not nomyap=='':
    edad=int(input('edad:'))
    mostrar(nomyap,edad)
    nomyap=str(input('Nombre y apellido:'))


    
