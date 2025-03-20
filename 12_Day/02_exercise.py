import random

# Ejercicio 1
def lista_de_colores_hexa(num_colores):
    colores_hexa = []
    for _ in range(num_colores):
        color = ''.join(random.choice('0123456789abcdef') for _ in range(6))
        colores_hexa.append(f'#{color}')
    return colores_hexa

print(lista_de_colores_hexa(5))


# Ejercicio 2
def lista_de_colores_rgb(num_colores):
    colores_rgb = []
    for _ in range(num_colores):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colores_rgb.append(f"rgb({r},{g},{b})")
    return colores_rgb

print(lista_de_colores_rgb(5))


# Ejercicio 3
def generar_colores(tipo, num_colores):
    if tipo == 'hexa':
        return lista_de_colores_hexa(num_colores)
    elif tipo == 'rgb':
        return lista_de_colores_rgb(num_colores)
    else:
        return "Tipo de color no válido. Elige 'hexa' o 'rgb'."
print(generar_colores('hexa', 5))
print(generar_colores('rgb', 5))
