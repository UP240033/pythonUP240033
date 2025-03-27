# 1
numeros = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos_o_cero = [n for n in numeros if n <= 0]
print(negativos_o_cero)

# 2
lista_de_listas = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
aplanada = [item for sublista in lista_de_listas for subsublista in sublista for item in subsublista]
print(aplanada)

# 3
tuplas = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(tuplas)

# 4
paises = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
paises_transformados = [[pais[0].upper(), pais[0][:3].upper(), ciudad.upper()] for pais_ciudad in paises for pais, ciudad in pais_ciudad]
print(paises_transformados)

# 5
diccionarios_paises = [{'pais': pais[0].upper(), 'ciudad': ciudad.upper()} for pais_ciudad in paises for pais, ciudad in pais_ciudad]
print(diccionarios_paises)

# 6
nombres = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
nombres_completos = [' '.join(nombre[0]) for nombre in nombres]
print(nombres_completos)

# 7
calcular_pendiente_interseccion = lambda x1, y1, x2, y2: ((y2 - y1) / (x2 - x1), y1 - ((y2 - y1) / (x2 - x1)) * x1)
print(calcular_pendiente_interseccion(1, 2, 3, 6))  