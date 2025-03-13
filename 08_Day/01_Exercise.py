# 1
dog = {}

# 2
dog['name'] = 'Paco'
dog['color'] = 'Marrón'
dog['breed'] = 'Golden Retriever'
dog['legs'] = 4
dog['age'] = 5

# 3
student = {
    'first_name': 'Alondra',
    'last_name': 'Martinez',
    'gender': 'Roque',
    'age': 18,
    'marital_status': 'Soltero',
    'skills': ['Python', 'Análisis de Datos'],
    'country': 'Mexico',
    'city': 'Aguascalientes',
    'address': 'Calle Principal 123'
}

# 4
student_length = len(student)
print(f"Longitud del diccionario student: {student_length}")

# 5
skills_value = student['skills']
print(f"Skills: {skills_value}")
print(f"Tipo de dato de skills: {type(skills_value)}")

# 6
student['skills'].append('Aprendizaje Automático')
student['skills'].append('SQL')
print(f"Skills actualizados: {student['skills']}")

# 7
keys_list = list(student.keys())
print(f"Claves: {keys_list}")

# 8
values_list = list(student.values())
print(f"Valores: {values_list}")

# 9
items_list = list(student.items())
print(f"Items (Lista de Tuplas): {items_list}")

# 10
del student['address']
print(f"Diccionario student después de eliminar 'address': {student}")

# 11
del student
