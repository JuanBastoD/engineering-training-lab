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
        if letra not in digitos:
            digitos[letra]=1
        else:
            digitos[letra]+=1
    return digitos

print(contar_digitos(112233)) #→ {1: 2, 2: 2, 3: 2}
print(contar_digitos(1000)) #→ {1: 1, 0: 3}
print(contar_digitos(555)) #→ {5: 3}
print(contar_digitos(-1234)) #→ {1: 1, 2: 1, 3: 1, 4: 1}
print(contar_digitos(0)) #→ {0: 1}