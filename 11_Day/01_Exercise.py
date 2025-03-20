#1
def sumar_dos_numeros(a, b):
    return a + b
print("Ejercicio 1: Sumar dos números")
print(sumar_dos_numeros(5, 7))  


# 2
import math
def area_de_circulo(r):
    return math.pi * r * r
print("\nEjercicio 2: Área de un círculo")
print(area_de_circulo(3))  


# 3
def sumar_todos_los_numeros(*args):
    if all(isinstance(x, (int, float)) for x in args):
        return sum(args)
    else:
        return "Todos los argumentos deben ser números"
print("\nEjercicio 3: Sumar todos los números")
print(sumar_todos_los_numeros(1, 2, 3, 4, 5)) 
print(sumar_todos_los_numeros(1, 2, "a", 4))  


# 4
def convertir_celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
print("\nEjercicio 4: Convertir Celsius a Fahrenheit")
print(convertir_celsius_a_fahrenheit(25))


# 5
def comprobar_estacion(mes):
    estaciones = {
        1: 'Invierno', 2: 'Invierno', 3: 'Primavera', 4: 'Primavera', 5: 'Primavera', 6: 'Verano',
        7: 'Verano', 8: 'Verano', 9: 'Otoño', 10: 'Otoño', 11: 'Otoño', 12: 'Invierno'
    }
    return estaciones.get(mes, "Mes no válido")
print("\nEjercicio 5: Comprobar estación")
print(comprobar_estacion(3))  
print(comprobar_estacion(12)) 
print(comprobar_estacion(15))

# 6
def calcular_pendiente(x1, y1, x2, y2):
    if x1 != x2:
        return (y2 - y1) / (x2 - x1)
    else:
        return "La pendiente está indefinida (línea vertical)"
print("\nEjercicio 6: Calcular pendiente")
print(calcular_pendiente(1, 2, 3, 4))  
print(calcular_pendiente(1, 2, 1, 4))  


# 7
import math
def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return raiz1, raiz2
    elif discriminante == 0:
        raiz = -b / (2*a)
        return raiz
    else:
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(-discriminante) / (2*a)
        return parte_real + parte_imaginaria * 1j, parte_real - parte_imaginaria * 1j
print("\nEjercicio 7: Resolver ecuación cuadrática")
print(resolver_ecuacion_cuadratica(1, -3, 2)) 


#8
def imprimir_lista(lst):
    for item in lst:
        print(item)
print("\nEjercicio 8: Imprimir lista")
imprimir_lista([1, 2, 3, 4])  


# 9
def invertir_lista(lst):
    lista_invertida = []
    for i in range(len(lst)-1, -1, -1):
        lista_invertida.append(lst[i])
    return lista_invertida
print("\nEjercicio 9: Invertir lista")
print(invertir_lista([1, 2, 3, 4, 5]))  


#10
def capitalizar_elementos_de_lista(lst):
    return [item.capitalize() for item in lst]
print("\nEjercicio 10: Capitalizar lista")
print(capitalizar_elementos_de_lista(["manzana", "pera", "plátano"]))  


# 11
def añadir_item(lst, item):
    lst.append(item)
    return lst
print("\nEjercicio 11: Añadir un ítem")
print(añadir_item([1, 2, 3], 4))  

# 12
def eliminar_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst
print("\nEjercicio 12: Eliminar un ítem")
print(eliminar_item([1, 2, 3], 2))  


# 13
def suma_de_numeros(n):
    return sum(range(1, n + 1))
print("\nEjercicio 13: Sumar números en un rango")
print(suma_de_numeros(5))  
print(suma_de_numeros(10))  


# 14
def suma_de_impares(n):
    return sum(i for i in range(1, n + 1) if i % 2 != 0)
print("\nEjercicio 14: Sumar números impares")
print(suma_de_impares(10))  

# 15
def suma_de_pares(n):
    return sum(i for i in range(1, n + 1) if i % 2 == 0)
print("\nEjercicio 15: Sumar números pares")
print(suma_de_pares(10)) 

