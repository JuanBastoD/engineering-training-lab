# Escribe una función invertir_numero(num) que devuelva el número con sus dígitos en orden inverso.
# Reglas:

# No uses slicing de strings ([::-1]).
# Usa solo bucles y aritmética (módulo %, división //).
# La función debe devolver un entero, no un string.

def invertir_numero(num):
    base = 10
    nuevo = 0
    aux = abs(num)
    while aux!=0:
        ultimo = aux % 10
        aux = aux // 10
        nuevo = (nuevo*base)+ultimo
        
    if num<0:
        return nuevo*-1
    else:
        return nuevo

print(invertir_numero(12345))
print(invertir_numero(1000))
print(invertir_numero(-456))
print(invertir_numero(0))
print(invertir_numero(7))