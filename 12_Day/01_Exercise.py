import random
import string

# Ejercicio 1
def generar_id_usuario_aleatorio():
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(6))

print(generar_id_usuario_aleatorio())


# Ejercicio 2
def generar_id_usuario_por_usuario():
    longitud = int(input("Ingrese el número de caracteres para cada ID: "))
    num_ids = int(input("Ingrese el número de IDs a generar: "))
    
    caracteres = string.ascii_letters + string.digits
    ids_usuario = []
    
    for _ in range(num_ids):
        ids_usuario.append(''.join(random.choice(caracteres) for _ in range(longitud)))
    
    return '\n'.join(ids_usuario)

print(generar_id_usuario_por_usuario())


# Ejercicio 3
def generar_color_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(generar_color_rgb())
