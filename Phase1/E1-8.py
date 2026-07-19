# Escribe una función contar_vocales_consonantes(texto) que devuelva un diccionario con el conteo de vocales y consonantes en un texto.
# Reglas:

# No distingue mayúsculas/minúsculas (trata 'A' y 'a' como la misma vocal).
# Solo cuenta letras (ignora espacios, números, puntuación).
# Devuelve un diccionario con dos claves: 'vocales' y 'consonantes'.

def contar_vocales_consonantes(palabra):
    vocales ="aeiou"
    diccionario ={'vocales':0, 'consonantes':0}
    palabra = palabra.lower()
    for letra in palabra:
        if letra.isalpha():
            if letra in vocales :
                diccionario['vocales']+=1 
            else:
                diccionario['consonantes']+=1
            
    return diccionario

print(contar_vocales_consonantes("Hola mundo"))