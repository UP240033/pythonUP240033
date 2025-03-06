# 1
lista_vacia = []

# 2
lista_mayor_5 = [1, 2, 3, 4, 5, 6]

# 3
print(len(lista_mayor_5))

# 4
primer_elemento = lista_mayor_5[0]
elemento_medio = lista_mayor_5[len(lista_mayor_5)//2]
ultimo_elemento = lista_mayor_5[-1]
print(primer_elemento, elemento_medio, ultimo_elemento)

# 5
tipos_de_datos_mixtos = ['Alondra', 18, 1.67, 'Soltero', 'Mexico']

# 6
empresas_tic = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7
print(empresas_tic)

# 8
print(len(empresas_tic))

# 9
print(empresas_tic[0], empresas_tic[len(empresas_tic)//2], empresas_tic[-1])

# 10
empresas_tic[0] = 'Meta'
print(empresas_tic)

# 11
empresas_tic.append('Twitter')
print(empresas_tic)

# 12
empresas_tic.insert(len(empresas_tic)//2, 'Snapchat')
print(empresas_tic)

# 13
empresas_tic[1] = empresas_tic[1].upper()
print(empresas_tic)

# 14
print('#;  '.join(empresas_tic))

# 15
print('Google' in empresas_tic)

# 16
empresas_tic.sort()
print(empresas_tic)

# 17
empresas_tic.reverse()
print(empresas_tic)

# 18
print(empresas_tic[:3])

# 19
print(empresas_tic[-3:])

# 20
print(empresas_tic[len(empresas_tic)//2-1:len(empresas_tic)//2+1])

# 21
empresas_tic.pop(0)
print(empresas_tic)

# 22
empresas_tic.pop(len(empresas_tic)//2)
print(empresas_tic)

# 23
empresas_tic.pop(-1)
print(empresas_tic)

# 24
empresas_tic.clear()
print(empresas_tic)

# 25
del empresas_tic

# 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# 27
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)

