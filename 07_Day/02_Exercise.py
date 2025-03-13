#1
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}


union = A.union(B)
print(f"Unión de A y B: {union}")


interseccion = A.intersection(B)
print(f"Intersección de A y B: {interseccion}")


es_subconjunto = A.issubset(B)
print(f"¿A es subconjunto de B? {es_subconjunto}")


son_disjuntos = A.isdisjoint(B)
print(f"¿A y B son conjuntos disjuntos? {son_disjuntos}")


union_AB = A.union(B)
union_BA = B.union(A)
print(f"Unión de A con B: {union_AB}")
print(f"Unión de B con A: {union_BA}")


diferencia_simetrica = A.symmetric_difference(B)
print(f"Diferencia simétrica entre A y B: {diferencia_simetrica}")


del A
del B
print("Conjuntos A y B eliminados")
