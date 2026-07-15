# función que cuente cuántas veces aparece cada dígito (0–9) 
# en un número. Devuelve un diccionario con formato {dígito: 
# cantidad}. Ignora números negativos (trata el signo como no 
# existente).
   
# d = {}
# d.get('x', 0)       # ¿Qué devuelve si 'x' no existe?
# d['x'] = d.get('x', 0) + 1
# print(d)

def contar_digitos(num):
    absoluto = abs(num)
    letras = str(absoluto)
    digitos = {}
    for letra in letras:
        entero= int(letra)
        digitos[entero] = digitos.get(entero,0) +1
    return digitos

print(contar_digitos(112233))
print(contar_digitos(1000))
print(contar_digitos(555))
print(contar_digitos(-1234))
print(contar_digitos(0))