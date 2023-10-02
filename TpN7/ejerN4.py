def cargar(vec):
    for i in range(len(vec)):
        rest = i % 2
        if rest == 0:
            vec[i]=1

vector= [0,0,0,0,0,0,0,0,0,0]

cargar(vector)
print(vector)