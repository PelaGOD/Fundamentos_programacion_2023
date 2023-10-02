from math import sqrt

cat1 = float(input('Ingrese el valor del cateto 1: '))
cat2 = float(input('Ingrese el valor del cateto 2: '))

hip= sqrt((cat1**2)+(cat2**2))

print('La longitud del cuadrado es de :',hip)

area = hip**2

print('El area del cuadrado es :',area)