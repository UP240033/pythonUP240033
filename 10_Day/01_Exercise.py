# Ejercicio 1
for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1


# Ejercicio 2
for i in range(10, -1, -1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i -= 1


# Ejercicio 3
for i in range(1, 8):
    print('#' * i)


# Ejercicio 4
for i in range(8):
    print('# ' * 8)


# Ejercicio 5
for i in range(11):
    print(f"{i} x {i} = {i * i}")


# Ejercicio 6
lista = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in lista:
    print(item)


# Ejercicio 7
for i in range(101):
    if i % 2 == 0:
        print(i)


# Ejercicio 8
for i in range(101):
    if i % 2 != 0:
        print(i)
