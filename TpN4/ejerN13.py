from datetime import date

año=int(input('Ingrese el año: '))
mes=int(input('Ingrese el mes: '))
dia=int(input('Ingrese el dia: '))

datos = date(año,mes,dia)
print(datos)
dianow=int
dianow=dia+1
datos= date(año,mes,dianow)
print(datos)