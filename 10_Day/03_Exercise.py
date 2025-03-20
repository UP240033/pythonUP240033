# Ejercicio 1
lista_paises = ["Finland", "Iceland", "Thailand", "Sweden", "Denmark", "Germany", "Poland", "New Zealand"]
for pais in lista_paises:
    if 'land' in pais:
        print(pais)


# Ejercicio 2
frutas = ['banana', 'naranja', 'mango', 'limón']
for i in range(len(frutas) // 2):
    frutas[i], frutas[len(frutas) - 1 - i] = frutas[len(frutas) - 1 - i], frutas[i]
print(frutas)


# Ejercicio 3
lenguajes = ['Español', 'Inglés', 'Mandarín', 'Hindi', 'Árabe', 'Francés', 'Ruso', 'Alemán', 'Portugués', 'Japonés']
print(f'El número total de lenguas es: {len(set(lenguajes))}')


# Ejercicio 4
lenguajes_mas_hablados = {
    'Español': 460000000,
    'Inglés': 380000000,
    'Mandarín': 920000000,
    'Hindi': 340000000,
    'Árabe': 310000000,
    'Francés': 250000000,
    'Ruso': 150000000,
    'Alemán': 100000000,
    'Portugués': 220000000,
    'Japonés': 125000000
}
lenguajes_mas_hablados = sorted(lenguajes_mas_hablados.items(), key=lambda x: x[1], reverse=True)[:10]
for idioma, hablantes in lenguajes_mas_hablados:
    print(f'{idioma}: {hablantes} hablantes')


# Ejercicio 5
paises_mas_poblados = {
    'China': 1403500365,
    'India': 1366417754,
    'EE.UU.': 329484123,
    'Indonesia': 266911900,
    'Pakistán': 225199937,
    'Brasil': 212559417,
    'Nigeria': 206139589,
    'Bangladesh': 164689383,
    'Rusia': 145912025,
    'México': 127575529
}
paises_mas_poblados = sorted(paises_mas_poblados.items(), key=lambda x: x[1], reverse=True)[:10]
for pais, poblacion in paises_mas_poblados:
    print(f'{pais}: {poblacion} habitantes')



