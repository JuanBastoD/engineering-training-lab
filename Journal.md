# Diario de Entrenamiento

## Día 1 — Fase 0, Ejercicio D1

**Fecha:** [10/07/2026]
**Tiempo total:** 56 minutos (22 + 26 + 8)
**Ejecuciones fallidas:** 18
**Veredicto:** Aprobado con observaciones

### Qué aprendí
- Diferencia entre `print()` y `return`
- Cómo recorrer listas con `for x in lista`
- Inicializar variables fuera del bucle, no dentro
- Consistencia de tipos en el valor devuelto

### Errores cometidos
1. Usé `range(lista)` en lugar de `range(len(lista))` o `for x in lista`
2. Intenté modificar variables globales dentro de la función
3. Comparaba la lista completa en lugar de elementos individuales
4. Inicializaba `minimo` en cada vuelta del bucle

### Qué investigué
- Cómo definir diccionarios
- Sentencia `for` y función `range()`
- Documentación oficial de Python (10 min aprox)

### Reflexión
El problema no fue sintaxis — fue lógica de flujo. Una vez que entendí qué recorrer y dónde inicializar variables, el código salió. Necesito practicar este patrón más.

### Siguiente paso
D2: lectura de archivos, parseo, manejo de errores.


## Día 2 — Fase 0, Ejercicio D2

**Fecha:** [10/07/2026]
**Tiempo total:** 50 minutos 
**Ejecuciones fallidas:** 14 (6 de sintaxis + 8 de lógica)
**Veredicto:** Aprobado

### Qué aprendí
- Manejo de lineas rotas
- Conversion al formato corrercto
- Metodos de string .split('') y .strip('')
- Manejo de diccionarios de diccionarios

### Errores cometidos
1. No asigné a ninguna variable el elemento que dividí en partes
2. Acceder a indices sin haberlos divido
3. La clave del diccionario sobrescribiendose en el bucle


### Qué investigué
- Errores y excepciones (Aun no lo domino)
- Metodos .split('') y .strip('')
- Lectura y escritura de archivos open('', '', encode="utf-8")
- Documentación oficial de Python (20-25 min aprox)

### Reflexión
El problema fue sobre todo como abrir los archivos, asignar los valores a una lista, despues los pude dividir, formatear al tipo correcto. Luego necesité ayuda para crear el diccionario de diccionarios, debo practicarlo mas para familiarizarme con el manejo y modificacion según las claves.

### Siguiente paso
D3: validar si una cadena con ()[]{} está balanceada.