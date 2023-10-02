try:
    number = int(input("Ingrese un numero de 3 digitos: "))
    if 100 <= number <= 999:
        num_str= str(number)
        num_digits= len(num_str)
        armstrong_sum = sum(int(digit)** num_digits for digit in num_str)

        if armstrong_sum == number:
            print(f'{number} es un numero Armstrong')
        else: print(f'{number} no es un numero Armstrong')

    else: print('el numero debe ser de 3 digitos (100 hasta 999)')

except ValueError:
    print('por favor, ingrese un numero valido') 