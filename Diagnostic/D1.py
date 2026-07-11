"""
escribe una función que reciba una lista de enteros y devuelva un
diccionario con cuatro claves: mínimo, máximo, promedio y cantidad de
números pares. Prohibido usar min(), max() y sum(). Solo bucles y
condicionales. Decide tú qué hacer si la lista llega vacía, y justifica
tu decisión en un comentario.
"""
#busqué como definir listas
#busqué  como definir diccionarios

def limitesDeLista(lista):
    
    if lista==[]:
        salida = dict(Maximo=0, Minimo=0, Promedio=0, Pares=0)
        return salida
    
    maxi=prom=suma=par=0
    mini=lista[0]
    contador=0
    
    for x in lista:
        if x%2==0:
            par+=1
        if x>maxi:
            maxi=x
        if x<mini:
            mini=x
        suma+=x
        contador+=1

    prom= suma/contador
    salida = dict(Maximo=maxi, Minimo=mini, Promedio=prom, Pares=par)
    return salida

numeros = [100, 9, 1, 16,4, 25, 36, 49, 64, 81, 86]
numeros1 = [5,10,3]
numeros2 = []
print(limitesDeLista(numeros))
print(limitesDeLista(numeros1))
print(limitesDeLista(numeros2))

