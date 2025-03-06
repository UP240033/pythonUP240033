# 1. 
miembros_de_la_familia = ('Javier', 'Emiliano', 'Ely', 'Camila', 'Javier', 'Natalia') 
hermanos, padre, madre = miembros_de_la_familia[:4], miembros_de_la_familia[4], miembros_de_la_familia[5]

# 2. 
frutas = ("manzana", "plátano", "naranja")
verduras = ("zanahoria", "espinaca", "papa")
productos_animales = ("huevo", "leche", "carne")

# 3. 
alimentos_tp = frutas + verduras + productos_animales
print("Tupla de alimentos:", alimentos_tp)

# 4. 
alimentos_lt = list(alimentos_tp)
print("Lista de alimentos:", alimentos_lt)

# 5. 
elemento_central = alimentos_tp[len(alimentos_tp) // 2]  
elementos_centrales = alimentos_lt[len(alimentos_lt) // 2]  

print("Elemento central (tupla):", elemento_central)
print("Elemento central (lista):", elementos_centrales)

# 6.
primeros_tres_elementos = alimentos_lt[:3]
ultimos_tres_elementos = alimentos_lt[-3:]

print("Primeros tres elementos de la lista:", primeros_tres_elementos)
print("Últimos tres elementos de la lista:", ultimos_tres_elementos)

# 7.
del alimentos_tp

# 8. 
paises_nordicos = ('Suecia', 'Noruega', 'Dinamarca', 'Finlandia', 'Islandia')  
existe_elemento = 'Islandia' in paises_nordicos
print("¿Islandia es un país nórdico?", existe_elemento)

estonia_es_nordico = 'Estonia' in paises_nordicos
print("¿Estonia es un país nórdico?", estonia_es_nordico)
islandia_es_nordico = 'Islandia' in paises_nordicos
print("¿Islandia es un país nórdico?", islandia_es_nordico)
