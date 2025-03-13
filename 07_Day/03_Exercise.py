# 1. 
edades_lista = [18, 22, 22, 19, 18, 25, 30]
edades_conjunto = set(edades_lista)


longitud_lista = len(edades_lista)
longitud_conjunto = len(edades_conjunto)

print(f"Longitud de la lista: {longitud_lista}")
print(f"Longitud del conjunto: {longitud_conjunto}")

if longitud_lista > longitud_conjunto:
    print("La lista es más grande que el conjunto.")
elif longitud_lista < longitud_conjunto:
    print("El conjunto es más grande que la lista.")
else:
    print("La lista y el conjunto tienen la misma longitud.")



oracion = "Soy un maestro y me encanta inspirar y enseñar a las personas"
palabras = set(oracion.split())


numero_palabras_unicas = len(palabras)
print(f"El número de palabras únicas en la oración es: {numero_palabras_unicas}")
