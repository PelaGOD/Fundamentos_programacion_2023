cantP = int(input('Cantidad de alumnos promocionados: '))
cantR = int(input('Cantidad de alumnos regulares: '))
cantD = int(input('Cantidad de alumnos desaprobados: '))
cantL = int(input('Cantidad de alumnos Libres: '))

totA = cantD+cantL+cantP+cantR

porcP = (cantP*100)/totA
porcR = (cantR*100)/totA
porcD = (cantD*100)/totA
porcL = (cantL*100)/totA

print('porcentaje de alumnos promocionados: ',porcP)
print('porcentaje de alumnos regulares: ',porcR)
print('porcentaje de alumnos desaprobados: ',porcD)
print('porcentaje de alumnos libres : ',porcL)