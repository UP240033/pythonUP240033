# 1
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 2
edades.sort()
edad_minima = edades[0]
edad_maxima = edades[-1]
print("Edad mínima:", edad_minima)
print("Edad máxima:", edad_maxima)

edades.append(edad_minima)
edades.append(edad_maxima)
print("Lista de edades con la edad mínima y máxima añadidas:", edades)

if len(edades) % 2 == 0:
    edad_media = (edades[len(edades)//2 - 1] + edades[len(edades)//2]) / 2
else:
    edad_media = edades[len(edades)//2]
print("Edad media:", edad_media)

edad_promedio = sum(edades) / len(edades)
print("Edad promedio:", edad_promedio)

rango_de_edades = edad_maxima - edad_minima
print("Rango de edades:", rango_de_edades)

diferencia_minima = abs(edad_minima - edad_promedio)
diferencia_maxima = abs(edad_maxima - edad_promedio)
print("Diferencia absoluta entre min y promedio:", diferencia_minima)
print("Diferencia absoluta entre max y promedio:", diferencia_maxima)

# 2
paises = ['China', 'Rusia', 'EE.UU.', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']
#3
if len(paises) % 2 == 0:
    paises_del_medio = paises[len(paises)//2 - 1:len(paises)//2 + 1]
else:
    paises_del_medio = paises[len(paises)//2]
print("País(es) del medio:", paises_del_medio)

mitad_longitud = len(paises) // 2
if len(paises) % 2 == 0:
    primera_mitad = paises[:mitad_longitud]
    segunda_mitad = paises[mitad_longitud:]
else:
    primera_mitad = paises[:mitad_longitud + 1]
    segunda_mitad = paises[mitad_longitud + 1:]
print("Primera mitad de países:", primera_mitad)
print("Segunda mitad de países:", segunda_mitad)

#4
primeros_tres, *paises_escandinavos = paises
print("Primeros tres países:", primeros_tres)
print("Países escandinavos:", paises_escandinavos)
