# 1. 
empresas_ti = {'Google', 'Facebook', 'Amazon', 'Microsoft', 'Apple'}


longitud = len(empresas_ti)
print(f"Longitud del conjunto: {longitud}")


empresas_ti.add('Twitter')
print(f"Conjunto después de añadir 'Twitter': {empresas_ti}")


empresas_ti.update({'Netflix', 'Snapchat', 'LinkedIn'})
print(f"Conjunto después de añadir múltiples empresas: {empresas_ti}")


empresas_ti.remove('Facebook')
print(f"Conjunto después de eliminar 'Facebook': {empresas_ti}")


try:
    empresas_ti.remove('Tiktok')
except KeyError:
    print("Error: 'Tiktok' no encontrada, no se puede eliminar.")


empresas_ti.discard('Tiktok')
print(f"Conjunto después de intentar descartar 'Tiktok': {empresas_ti}")
