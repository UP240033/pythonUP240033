import math
edad = 25  
altura = 1.75 
numero_complejo = 3 + 4j  

#Triangulo
base_triangulo = float(input("Ingresa la base: "))
altura_triangulo = float(input("Ingresa la altura: "))
area_triangulo = 0.5 * base_triangulo * altura_triangulo
print(f"El area del triangulo es {area_triangulo}")

lado1 = float(input("Ingresa el lado a: "))
lado2 = float(input("Ingresa el lado b: "))
lado3 = float(input("Ingresa el lado c: "))
perimetro_triangulo = lado1 + lado2 + lado3
print(f"El perimetro del triangulo es {perimetro_triangulo}")

#Rectangulo
longitud_rectangulo = float(input("Ingresa la longitud: "))
ancho_rectangulo = float(input("Ingresa el ancho: "))
area_rectangulo = longitud_rectangulo * ancho_rectangulo
perimetro_rectangulo = 2 * (longitud_rectangulo + ancho_rectangulo)
print(f"Area del rectangulo: {area_rectangulo}, Perimetro: {perimetro_rectangulo}")

#Circulo
radio_circulo = float(input("Ingresa el radio: "))
pi = 3.14
area_circulo = pi * radio_circulo ** 2
circunferencia_circulo = 2 * pi * radio_circulo
print(f"Area del circulo: {area_circulo}, Circunferencia: {circunferencia_circulo}")

#Calculo de pendiente e interseccion de una recta
pendiente = 2  
interseccion_y = -2  
interseccion_x = -interseccion_y / pendiente
print(f"Pendiente: {pendiente}, Interseccion en x: {interseccion_x}, Interseccion en y: {interseccion_y}")

#Calculo de la pendiente y distancia entre dos puntos
punto1_x, punto1_y = 2, 2
punto2_x, punto2_y = 6, 10
pendiente_calculada = (punto2_y - punto1_y) / (punto2_x - punto1_x)
distancia_puntos = math.sqrt((punto2_x - punto1_x) ** 2 + (punto2_y - punto1_y) ** 2)
print(f"Pendiente: {pendiente_calculada}, Distancia: {distancia_puntos}")

#Comparacion de pendientes
print(f"Comparacion de pendientes: {pendiente == pendiente_calculada}")

#Definicion y calculo de una ecuacion cuadratica
def ecuacion_cuadratica(x):
    return x**2 + 6*x + 9

valores_x = [-3, -2, -1, 0, 1, 2]
for valor_x in valores_x:
    valor_y = ecuacion_cuadratica(valor_x)
    print(f"x: {valor_x}, y: {valor_y}")

#Comprobacion de comparacion de longitudes de cadenas
print(len("python") != len("dragon"))

#Verificacion de la existencia de "on" en las palabras
print("on" in "python" and "on" in "dragon")

#Verificacion de la palabra "jerga" en una oracion
oracion = "Espero que este curso no este lleno de jerga"
print("jerga" in oracion)

#Comprobacion de si "on" no esta en las palabras
print("on" not in "python" and "on" not in "dragon")

#Conversion de longitud de una cadena a float y string
longitud_python = float(len("python"))
longitud_python_str = str(longitud_python)
print(f"Longitud como float: {longitud_python}, Como string: {longitud_python_str}")

#Verificacion de si un numero es par
numero = int(input("Ingresa un numero: "))
print(f"{numero} es par: {numero % 2 == 0}")

#Comparaciones
print(7 // 3 == int(2.7))
print(type("10") == type(10))
print(int(float('9.8')) == 10)

#Calculo del salario semanal
horas_trabajadas = float(input("Ingresa las horas trabajadas: "))
tarifa_por_hora = float(input("Ingresa la tarifa por hora: "))
salario_semanal = horas_trabajadas * tarifa_por_hora
print(f"Tu salario semanal es {salario_semanal}")

#Calculo de los segundos vividos
anos_vividos = int(input("Ingresa los anos que has vivido: "))
segundos_vividos = anos_vividos * 365 * 24 * 60 * 60
print(f"Has vivido {segundos_vividos} segundos.")

#Tablas
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
