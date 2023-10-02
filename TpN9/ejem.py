matriz=[[1,5],[4,0],[1,2],[3,4],[5,6]]
matriz1=[[9,0],[8,5],[5,7],[4,4],[1,2]]
resultado=[[0,0],[0,0],[0,0][0,0],[0,0]]

print(matriz)
print(matriz1)
for i in range(len(matriz)):
    for j in range(len(matriz)):
        resultado[i,j]=(matriz[i][j]+matriz1[i][j])

print(resultado)