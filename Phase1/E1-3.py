""" 
función que devuelva el máximo común divisor (MCD) de dos números usando el algoritmo de Euclides. No uses la función math.gcd().
"""
# Algoritmo de euclides:
# mcd(a, b):
#     mientras b != 0:
#       temp = b
#       b = a % b
#       a = temp
#     devuelve a

def maximo_comun_divisor(x,y):
    while y != 0:
        auxiliar = y
        y = x % y
        x = auxiliar
    return x
    
print( maximo_comun_divisor(48,18))
print( maximo_comun_divisor(100,50))
print( maximo_comun_divisor(17,19))
print( maximo_comun_divisor(0,5))