A=int
B=int

for i in range(8):
    char= str(input('Introduce caracter: '))
    char=char.lower()
    if char=='a':
        A+=1
    elif char=='*':
        B+=1
    
print(f'la cantidad de "a":${A}, y de "*":${B}')