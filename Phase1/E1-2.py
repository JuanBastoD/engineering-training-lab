"""
función que reciba un número y devuelva True si es una edad válida (entre 0 y 120), False en caso contrario. Si el input no es un número, devuelve False sin crashear.
"""
def es_edad_valida (edad):
    try:
        return edad>=0 and edad<=120
    except:
        return False

print(es_edad_valida(25))
print(es_edad_valida(0))
print(es_edad_valida(120)) 
print(es_edad_valida(121)) 
print(es_edad_valida(-5)) 
print(es_edad_valida("abc"))
print(es_edad_valida(None)) 