# Ejercicio 1
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(es_primo(7))  
print(es_primo(10))  


# Ejercicio 2
def son_elementos_unicos(lst):
    return len(lst) == len(set(lst))

print(son_elementos_unicos([1, 2, 3, 4, 5]))  
print(son_elementos_unicos([1, 2, 2, 4, 5]))  


# Ejercicio 3
def son_todos_del_mismo_tipo(lst):
    if not lst:  
        return True
    return all(isinstance(item, type(lst[0])) for item in lst)

print(son_todos_del_mismo_tipo([1, 2, 3, 4]))  
print(son_todos_del_mismo_tipo([1, 'a', 3, 4]))  


# Ejercicio 4
import re

def es_variable_valida(var):
    return bool(re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', var))

print(es_variable_valida("variable_valida"))  
print(es_variable_valida("1invalida"))  


# Ejercicio 5
def idiomas_mas_hablados():
    datos_idiomas = {
        "Inglés": 1500,
        "Mandarín": 1200,
        "Hindi": 600,
        "Español": 500,
        "Francés": 300,
        "Árabe": 300,
        "Bengalí": 250,
        "Portugués": 240,
        "Ruso": 150,
        "Japonés": 125,
        "Lahnda (Punjabi)": 120,
        "Turco": 110,
        "Coreano": 100,
        "Alemán": 90,
        "Vietnamita": 85
    }
    idiomas_ordenados = sorted(datos_idiomas.items(), key=lambda x: x[1], reverse=True)
    return idiomas_ordenados[:10]  

print(idiomas_mas_hablados())


# Ejercicio 6
def paises_mas_poblados():
    datos_paises = {
        "China": 1400000000,
        "India": 1300000000,
        "Estados Unidos": 330000000,
        "Indonesia": 270000000,
        "Pakistán": 220000000,
        "Brasil": 210000000,
        "Nigeria": 200000000,
        "Bangladesh": 160000000,
        "Rusia": 145000000,
        "México": 130000000,
        "Japón": 125000000,
        "Etiopía": 115000000,
        "Filipinas": 110000000,
        "Egipto": 100000000,
        "Vietnam": 96000000
    }
    paises_ordenados = sorted(datos_paises.items(), key=lambda x: x[1], reverse=True)
    return paises_ordenados[:10]  

print(paises_mas_poblados())
