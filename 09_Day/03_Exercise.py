#1
persona = {
    'nombre': 'Alondra',
    'edad': 18,
    'ciudad': 'Aguascalientes',
    'ocupacion': 'Ingeniero',
    'telefono': '123-456-789',
    'direccion': 'Calle 123'
}
#2
persona['edad'] = 18
persona['ocupacion'] = 'Arquitecto'
persona['correo'] = 'alondr@mail.com'

print("Diccionario modificado:", persona)

print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona['edad']}")
print(f"Correo: {persona['correo']}")

del persona['telefono']
print("Diccionario después de eliminar teléfono:", persona)

if 'direccion' in persona:
    print(f"La dirección es: {persona['direccion']}")
else:
    print("No se encontró la dirección.")
