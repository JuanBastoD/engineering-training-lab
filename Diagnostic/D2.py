f = open('datos.txt','r',encoding="utf-8")
lineas = f.readlines()
ciudades = {} # se crea el diccionario
for linea in lineas:
    partes=linea.split(',')
    ciudad = partes[2].strip('\n') #le quito el indicador de salto de linea que hace queden diferentes algunas ciudades
    try:
        edad = int(partes[1])
    except:
        # Si falla, ignora esta línea y continúa
        continue
    
    if ciudad not in ciudades:
        ciudades[ciudad] = {'suma':0 ,'cantidad':0} #si es la primera vez que sale la ciudad en la linea se inicializa en cero
    ciudades[ciudad]['suma'] +=edad # se acumula la edad de la linea que se está leyendo
    ciudades[ciudad]['cantidad']+=1 # se acumula un contador para luego sacar el promedio

for ciudad, datos in ciudades.items():
    promedio = datos['suma'] / datos['cantidad']
    ciudades[ciudad] = promedio

print (ciudades)


