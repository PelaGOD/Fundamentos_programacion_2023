def positivo_o_negativo(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'

# Pruebas de la función
numero1 = 5
resultado1 = positivo_o_negativo(numero1)
print(f"El resultado para el número {numero1} es: {resultado1}")

numero2 = -2
resultado2 = positivo_o_negativo(numero2)
print(f"El resultado para el número {numero2} es: {resultado2}")

numero3 = 0
resultado3 = positivo_o_negativo(numero3)
print(f"El resultado para el número {numero3} es: {resultado3}")
