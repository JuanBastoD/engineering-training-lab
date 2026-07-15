# Funcion que convierta C a F
# Formula: F = (C * 9/5) + 32

def celsius_a_fahrenheit (celsius):
    return round(float((celsius * 9/5)+32),1)

print(celsius_a_fahrenheit(0))
print(celsius_a_fahrenheit(100))
print(celsius_a_fahrenheit(-43.4567))

"""
Resumen: 
primera ejecucion fallada: olvide poner el print
segunda ejecuion fue correcta pero no habia redondeado
luego investigue la funcion round
tercera ejecuion correcta
"""
