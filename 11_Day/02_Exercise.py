# Ejercicio 1
def evens_and_odds(n):
    even_count = 0
    odd_count = 0
    for i in range(n+1):
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return f"The number of evens are {even_count}. The number of odds are {odd_count}."

print("Ejercicio 1: Contar pares e impares")
print(evens_and_odds(100))


# Ejercicio 2
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print("\nEjercicio 2: Calcular factorial")
print(factorial(5))
print(factorial(0))


# Ejercicio 3
def is_empty(value):
    if value == "" or value == [] or value == {} or value == 0 or value is None:
        return True
    return False

print("\nEjercicio 3: Comprobar si está vacío")
print(is_empty(""))  
print(is_empty([1, 2, 3]))  
print(is_empty(None))  


# Ejercicio 4
def calculate_mean(lst):
    if len(lst) == 0:
        return "List is empty"
    return sum(lst) / len(lst)

print("\nEjercicio 4: Calcular media")
print(calculate_mean([1, 2, 3, 4, 5]))  


# Ejercicio 5
def calculate_median(lst):
    if len(lst) == 0:
        return "List is empty"
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

print("\nEjercicio 5: Calcular mediana")
print(calculate_median([1, 2, 3, 4, 5]))  
print(calculate_median([1, 2, 3, 4]))  


# Ejercicio 6
from collections import Counter

def calculate_mode(lst):
    if len(lst) == 0:
        return "List is empty"
    count = Counter(lst)
    mode_data = count.most_common(1)
    return mode_data[0][0] if mode_data else "No mode"

print("\nEjercicio 6: Calcular moda")
print(calculate_mode([1, 2, 2, 3, 4, 5]))  
print(calculate_mode([1, 1, 2, 2, 3, 3]))  


# Ejercicio 7
def calculate_range(lst):
    if len(lst) == 0:
        return "List is empty"
    return max(lst) - min(lst)

print("\nEjercicio 7: Calcular rango")
print(calculate_range([1, 2, 3, 4, 5]))  


# Ejercicio 8
def calculate_variance(lst):
    if len(lst) == 0:
        return "List is empty"
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

print("\nEjercicio 8: Calcular varianza")
print(calculate_variance([1, 2, 3, 4, 5]))  


# Ejercicio 9
import math
def calculate_std(lst):
    if len(lst) == 0:
        return "List is empty"
    variance = calculate_variance(lst)
    return math.sqrt(variance)

print("\nEjercicio 9: Calcular desviación estándar")
print(calculate_std([1, 2, 3, 4, 5]))  
