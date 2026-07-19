# Un número de Armstrong (también llamado narcisista) es aquel que es igual a la suma de sus propios dígitos elevados a la potencia del número de dígitos.
# Ejemplos: 

# 153 es Armstrong: 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 ✓
# 9474 es Armstrong: 9⁴ + 4⁴ + 7⁴ + 4⁴ = 6561 + 256 + 2401 + 256 = 9474 ✓
# 123 no es Armstrong: 1³ + 2³ + 3³ = 1 + 8 + 27 = 36 ≠ 123 ✗

# Escribe una función es_armstrong(num) que devuelva True si el número es de Armstrong, False en caso contrario.

def es_armstrong(num):
    aux = num
    digitos = []
    contador= 0
    armstrong = 0
    while aux!=0:
        ultimo = aux%10
        aux = aux//10
        digitos.append(ultimo)
        contador+= 1
    for numero in digitos:
        armstrong += numero**contador
    return num==armstrong
print(es_armstrong(153))
print(es_armstrong(123))
print(es_armstrong(9474))