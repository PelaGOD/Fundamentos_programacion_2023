mul= 1
sum = 0
i=20
rest=float
for i in range(50):
    num=i
    rest=num%2
    if rest == 0:
        mul=num*mul
        sum=num+sum

print(f'la suma es de:{sum} y la multiplicacion:{mul}')