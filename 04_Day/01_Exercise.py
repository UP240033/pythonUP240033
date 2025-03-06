# 1
cadena_1 = ''.join (['Thirty' , ' ' , 'Days' , ' ' , 'Of' , ' ' , 'Python'])
print(cadena_1)

# 2
cadena_2 = (['Coding' , ' ' , 'For' , ' ' , 'All'])
print(cadena_2)

# 3
empresa = "Coding For All"
print(empresa)

# 4
print(len(empresa))

# 5
print(empresa.upper())

# 6
print(empresa.lower())

# 7
print(empresa.capitalize())
print(empresa.title())
print(empresa.swapcase())

# 8
print(empresa[6:])

# 9
print(empresa.find("Coding") != -1)

# 10
print(empresa.replace('Coding', 'Python'))

# 11
cadena_3 = "Python for Everyone"
print(cadena_3.replace("Everyone", "All"))

# 12
print(empresa.split())

# 13
cadena_4 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(cadena_4.split(','))

# 14
print(empresa[0])

# 15
print(len(empresa) - 1)

# 16
print(empresa[10])

# 17
acronimo_1 = "PFE"
print(acronimo_1)

# 18
acronimo_2 = "CFA"
print(acronimo_2)

# 19
print(empresa.index('C'))

# 20
print(empresa.index('F'))

# 21
empresa_2 = "Coding For All People"
print(empresa_2.rfind('l'))

# 22
frase = 'You cannot end a sentence with because because because is a conjunction'
print(frase.find('because'))

# 23
print(frase.rindex('because'))

# 24
print(frase[33:60])

# 25
print(frase.find('because'))

# 26
print(frase[33:60])

# 27
print(empresa.startswith('Coding'))

# 28
print(empresa.endswith('coding'))

# 29
cadena_5 = '   Coding For All      '
print(cadena_5.strip())

# 30
variable_1 = "30DaysOfPython"
variable_2 = "thirty_days_of_python"
print(variable_1.isidentifier())
print(variable_2.isidentifier())

# 31
librerias = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(librerias))

# 32
print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\tAge\tCountry\tCity")#33
print("Alondra\t18\tMexico\tAguascalientes")#34

# 35
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# 36
print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6:.2f}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8 ** 6}")

