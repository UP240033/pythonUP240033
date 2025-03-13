# 1
mi_edad = int(input("Ingresa tu edad: "))
tu_edad = int(input("Ingresa mi edad: "))

if mi_edad > tu_edad:
    diferencia_edad = mi_edad - tu_edad
    if diferencia_edad == 1:
        print(f"Tengo {diferencia_edad} año más que tú.")
    else:
        print(f"Tengo {diferencia_edad} años más que tú.")
elif mi_edad < tu_edad:
    diferencia_edad = tu_edad - mi_edad
    if diferencia_edad == 1:
        print(f"Tú tienes {diferencia_edad} año más que yo.")
    else:
        print(f"Tú tienes {diferencia_edad} años más que yo.")
else:
    print("Tenemos la misma edad.")

#2
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres lo suficientemente mayor para conducir.")
else:
    años_restantes = 18 - edad
    print(f"Por favor, espera {años_restantes} años más para poder conducir.")

#3
# 1
a = int(input("Ingresa el primer número (a): "))
b = int(input("Ingresa el segundo número (b): "))

# 2
if a > b:
    print("a es mayor que b.")
elif a < b:
    print("a es menor que b.")
else:
    print("a es igual a b.")

