# Declaración de variables
nombre = "Alondra"
apellido = "Martínez"
nombre_completo = "Alondra Martínez"
país = "México"
ciudad = "Aguascalientes"
edad = 18
año = 2025
is_married = False
is_true = True

# Comprobar los tipos de datos
print("Tipo de nombre:", type(nombre))
print("Tipo de apellido:", type(apellido))
print("Tipo de nombre_completo:", type(nombre_completo))
print("Tipo de país:", type(país))
print("Tipo de ciudad:", type(ciudad))
print("Tipo de edad:", type(edad))
print("Tipo de año:", type(año))
print("Tipo de is_married:", type(is_married))
print("Tipo de is_true:", type(is_true))

# Longitud del nombre
print("Longitud del nombre:", len(nombre))

# Comparar longitud del nombre y apellido
print("Comparación de longitudes:", len(nombre) == len(apellido))

# Operaciones matemáticas
num_uno = 5
num_dos = 4

total = num_uno + num_dos
diff = num_uno - num_dos
producto = num_uno * num_dos
división = num_uno / num_dos
remainder = num_uno % num_dos
exp = num_uno ** num_dos
floor_division = num_uno // num_dos

# Mostrar resultados
print("Suma:", total)
print("Diferencia:", diff)
print("Producto:", producto)
print("División:", división)
print("Módulo:", remainder)
print("Exponenciación:", exp)
print("Floor Division:", floor_division)

# Cálculo de área y circunferencia de un círculo
radio = 30
pi=3.1416
area_del_circulo = pi * radio ** 2
circunferencia_del_circulo = 2 * pi * radio

print("Área del círculo:", area_del_circulo)
print("Circunferencia del círculo:", circunferencia_del_circulo)

# Entrada del usuario para calcular área de un círculo
radio_usuario = float(input("Ingrese el radio del círculo: "))
area_usuario = pi * radio_usuario ** 2
print("Área del círculo con radio ingresado:", area_usuario)

# Entrada del usuario para obtener datos personales
nombre_usuario = input("Ingrese su nombre: ")
apellido_usuario = input("Ingrese su apellido: ")
pais_usuario = input("Ingrese su país: ")
edad_usuario = int(input("Ingrese su edad: "))

print(f"Nombre: {nombre_usuario}, Apellido: {apellido_usuario}, País: {pais_usuario}, Edad: {edad_usuario}")

import keyword
print(keyword.kwlist)