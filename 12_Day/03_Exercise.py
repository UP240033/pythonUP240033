import random

# Ejercicio 1
def mezclar_lista(lista):
    random.shuffle(lista)
    return lista

print(mezclar_lista([1, 2, 3, 4, 5, 6]))


# Ejercicio 2
def numeros_aleatorios_unicos():
    return random.sample(range(10), 7)

print(numeros_aleatorios_unicos())
