# El algoritmo de Luhn es un método para validar números de tarjeta de crédito. Funciona así:

# De derecha a izquierda, duplica cada segundo dígito.
# Si el resultado de duplicar es mayor a 9, réstale 9.
# Suma todos los dígitos (los duplicados y ajustados + los que no se duplicaron).
# Si la suma es divisible por 10, el número es válido.

# Dígitos:     4  5  3  2  0  1  5  1  1  2  8  3  0  3  6  6
# Posición:    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
# (derecha a izquierda, posiciones pares se duplican)

# De derecha:  6  6  3  0  3  8  2  1  1  5  1  0  2  3  5  4
# Duplicar:       12    0    16    1    10    1    2    5    4
# Ajustar>9:      3     0    7     1    1     1    2    5    4

# Suma: 6 + 3 + 3 + 0 + 3 + 7 + 2 + 1 + 1 + 1 + 1 + 0 + 2 + 3 + 5 + 4 = 42

# 42 % 10 = 2 (no divisible por 10) → INVÁLIDO

def validar_tarjeta(num):
    digitos =[]
    while num!=0:
        ultimo = num%10
        num = num//10
        digitos.append(ultimo)
    posi=1
    luhn=0
    for numero in digitos:
        if posi%2==0:
            duplicar = numero*2
            if duplicar>9:
                duplicar= duplicar-9
            luhn+=duplicar
        else:
            luhn+=numero
        posi+=1
    return luhn%10==0

print(validar_tarjeta(4532015112830366))
print(validar_tarjeta(4532015112830365))
print(validar_tarjeta(79927398713))
print(validar_tarjeta(79927398714))