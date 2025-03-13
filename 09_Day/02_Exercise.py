# 1
puntaje = float(input("Ingresa tu puntaje: "))

if puntaje >= 90:
    print("Calificación: A")
elif puntaje >= 80:
    print("Calificación: B")
elif puntaje >= 70:
    print("Calificación: C")
elif puntaje >= 60:
    print("Calificación: D")
else:
    print("Calificación: F")

#2

mes = input("Ingresa el mes (por ejemplo, 'Septiembre'): ").capitalize()

if mes in ['Septiembre', 'Octubre', 'Noviembre']:
    print("La estación es Otoño.")
elif mes in ['Diciembre', 'Enero', 'Febrero']:
    print("La estación es Invierno.")
elif mes in ['Marzo', 'Abril', 'Mayo']:
    print("La estación es Primavera.")
elif mes in ['Junio', 'Julio', 'Agosto']:
    print("La estación es Verano.")
else:
    print("Mes no válido. Por favor ingresa un mes correcto.")

#3
frutas = ['plátano', 'naranja', 'mango', 'limón']

print("Lista completa de frutas:", frutas)

print("La primera fruta es:", frutas[0])

frutas.append('manzana')  
print("Lista después de agregar 'manzana':", frutas)

frutas.remove('naranja')  
print("Lista después de eliminar 'naranja':", frutas)

print("Lista ordenada alfabéticamente:", frutas)

if 'mango' in frutas:
    print("La fruta 'mango' está en la lista.")
else:
    print("La fruta 'mango' no está en la lista.")

print("Recorriendo la lista de frutas:")
for fruta in frutas:
    print(fruta)

print("Número de frutas en la lista:", len(frutas))
