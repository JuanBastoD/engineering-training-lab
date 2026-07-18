# Una contraseña es válida si cumple todas estas condiciones:

# Tiene al menos 8 caracteres
# Contiene al menos una mayúscula
# Contiene al menos una minúscula
# Contiene al menos un dígito
# Contiene al menos un carácter especial (de este conjunto: !@#$%^&*)

"""
investigue: .islower .isupper y busque si la forma correcta de comparar strings era con == pero no encontre lo que buscaba
"""

def validar_contrasena(pasword):
    mayus = False
    minus = False
    digit = False
    special = False
    group = ['!','@','#','$','%','^','&','*']
    if len(pasword)<8:
        return False
    
    for character in pasword:
        for spe in group:
            if character==spe:
                special= True
        if character.islower():
            minus = True
        elif character.isupper():
            mayus = True
        elif character.isdigit():
            digit = True
    
    return mayus and minus and digit and special

print(validar_contrasena("Abc123!@"))
print(validar_contrasena("abc123!@"))
print(validar_contrasena("ABC123!@"))
print(validar_contrasena("Abc!@"))
print(validar_contrasena("Abcdefgh"))
print(validar_contrasena(""))