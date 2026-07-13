# stack =[1,2,3]
# a = stack.pop()
# print(a)  #prueba de que al eliminar puedo guardar la variable para verificar
#busque en la documentacion la funcion enumerate

def balanceado (cadena):
    stack = []
    if cadena=="":
        return True
    # if cadena[0]==')' or cadena[0]==']' or cadena[0]=='}':
    #         return False
    # elif cadena[-1]=='(' or cadena[-1]=='[' or cadena[-1]=='{':
    #         return False
    def vacio(stack):
        return len(stack)==0
    
    for i, caracter in enumerate(cadena):
        if caracter==')':
            if vacio(stack):return False
            apertura = stack.pop()
            if apertura!='(':
                return False
        elif caracter==']':
            if vacio(stack):return False
            apertura = stack.pop()
            if apertura!='[':
                return False
        elif caracter=='}':
            if vacio(stack):return False
            apertura = stack.pop()
            if apertura!='{':
                return False
        else:
            stack.append(caracter)
      
    return len(stack)==0

cadena="([)]"
print(cadena, balanceado(cadena))
cadena="()[]{}"
print(cadena, balanceado(cadena))
cadena="([)]"
print(cadena, balanceado(cadena))

cadena="()"
print(cadena, balanceado(cadena))
cadena="([{}])"
print(cadena, balanceado(cadena))
cadena="([)]"
print(cadena, balanceado(cadena))
cadena="(()("
print(cadena, balanceado(cadena))
cadena=""
print(cadena, balanceado(cadena))
cadena="}"
print(cadena, balanceado(cadena))