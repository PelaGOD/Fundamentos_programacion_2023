c1,c2,c3 = int



for i in range(120):
    sistem=int(input('Ingrese el numero del sistema operativo que le gusta 1)windows, 2)linux, 3)ios: '))
    if sistem==1:
        c1+=1
    elif sistem==2:
        c2+=1
    else: c3+=1

if c1>c2 and c1>c3:
    print(f'el sistema mas votado es windows con ${c1}')
elif c2>c1 and c2>c3:
    print(f'el sistema mas votado es linux con ${c2}')
else: print(f'el sistema mas votado es ios ${c3}')