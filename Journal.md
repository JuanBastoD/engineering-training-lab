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


## Día 1 — Fase 0, Ejercicio D2

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

## Día 2 — Fase 0, Ejercicio D3

**Fecha:** [12/07/2026]
**Tiempo total:** 63 minutios 17 segundos 
**Ejecuciones fallidas:** 10 +7 de lógica
**Veredicto:** Aprobado

### Qué aprendí
- Estructura de datos: pila (stack) y cómo funciona (append() y pop())
- Cómo una pila resuelve problemas de orden/pareja (matching)
- Diferencia entre llamar una función y usar su valor devuelto
- Indexación negativa en strings/listas ([-1] para el último elemento)
- Importancia de validar estado antes de operaciones destructivas (pop() en lista vacía)
- Lógica de devoluciones en funciones anidadas



### Errores cometidos
1. Append antes de validar: metía el carácter en el stack antes de saber si era apertura o cierre
2. Ignorar valores devueltos: llamaba vacio(stack) pero no usaba el True/False que devolvía
3. Lógica invertida: devolvía False cuando debería devolver True (confundí el sentido)
4. No verificar al final: no validaba si el stack quedaba vacío después del bucle
5. Función incompleta: vacio() no devolvía nada en el caso falso (devolvía None implícitamente)


### Qué investigué
- Stack/pila en documentación oficial
- Métodos .pop() y .append() en listas
- Indexación negativa
- Funciones que devuelven valores y cómo usarlos
- ~15 min de documentación + experimentación en intérprete

### Reflexión
Los dos primeros ejercicios fueron sobre como hacer tal cosa en python, este D3 fue como pensar en un algoritmo . Luego que entendí que pila es ultimo en entrar primero en salir pude relacionarlo con brackets balanceados o sea que el ultimo que abrí debe ser el primero en cerrar. 

Fue frustrante hacer que todos los casos pasaran correctamente(18 ejecuciones), el orden importa, las funciones devuelven valores y estos deben utilizarse y debo validar el estado antes de hacer operaciones peligrosas (pop) .Son principios, no sintaxis

### Siguiente paso
Fase 1: Python básico sin IA. Entrenamiento de fluidez en variables, bucles, funciones, archivos.

## Dia 3 - Fase 1 Ejercicios 1-5

| **E** | **Tiempo** | **Ejecuciones** | **Veredicto** |
| --- | --- | --- | --- |
| E1.1 | 3 min | 3 | Aprobado |
| E1.2 | 9 min | 2 | Aprobado |
| E1.3 | 8 min | 2 | Aprobado |
| E1.4 | 17 min | 8 | Aprobado |
| E1.5 | 20 min | 6 | Aprobado |

### Que aprendí
- retorno de valores en una funcion sin usar tantas lineas
- redondeo de float
- retorno de booleanos sin necesidad de un sentencia if en la funcion
- como funciona el algoritmo de euclides
- manejo de casos base 
- sucesion de fibonacci
- las funciones abs(), str(), get()

### Errores cometidos
1. E1.1: usé `return print(...)` en lugar de solo `return` — confundí devolver con imprimir (mismo error que en D1)
2. E1.1: redondeé a 2 decimales en lugar de 1 — no leí el enunciado con cuidado
3. E1.4: el bucle no se detenía a tiempo — mi lógica calculaba un índice de más (F(5) me daba 8 en lugar de 5)
4. E1.4: al arreglar el desfase, tuve que agregar casos base para 0 y 1, si no el bucle rompía el conteo
5. E1.5: reutilicé el nombre del parámetro `num` para otra cosa dentro del bucle — funcionaba, pero era confuso

### Que investigué
**Documentacion oficial**
- round() — función built-in para redondear decimales (E1.1)
- try/except — manejo básico de excepciones para evitar crashes (E1.2)
- Conversión de tipos: int(), float() — para validar y convertir inputs (E1.2)
- Operadores de comparación encadenados (0 <= edad <= 120) — lo viste en mi observación de diseño, no en documentación, pero vale la pena que lo anotes como aprendizaje del día
- str() — conversión de número a string para iterar dígitos (E1.5)
- abs() — valor absoluto, para ignorar el signo negativo (E1.5)
- dict.get(clave, valor_default) — método de diccionarios para contar/acumular sin if/else explícito (E1.5)
- Iterar sobre un string (for caracter in texto) — reutilizaste este patrón de D3, no lo investigaste de nuevo, pero es un contenido que aplicaste

**Conceptos y algoritmos**
- Algoritmo de Euclides (MCD) — no es documentación de Python, sino un algoritmo matemático que ya conocías o revisaste conceptualmente (E1.3)
- Sucesión de Fibonacci — concepto revisado en FreeCodeCamp, no en docs de Python (E1.4)

### Reflexión

**Sobre E1.4 (Fibonacci):** Este ejercicio siempre me costó en la universidad. Tuve que volver a la estrategia de papel: anotar los valores y "compilar mentalmente" paso a paso antes de poder escribirlo en código. Es un patrón personal — cuando un ejercicio involucra seguir un estado que cambia en cada iteración (como ant/sig en Fibonacci, redes de petri o automatas), necesito verlo escrito a mano antes de confiar en mi cabeza. Lo voy a seguir usando como estrategia deliberada, no como señal de que algo anda mal.

**Sobre E1.5:** El tiempo alto (20 min) no fue por lógica — la entendí rápido gracias a D2(Ciudades de un archivo). Fue debugging visual: nombres de variables mal puestos, revisar outputs con cuidado. Diferencia importante para mí: "no entender el problema" y "cometer errores de descuido" se sienten distinto y debo distinguirlos al anotar, porque piden soluciones distintas.

**Sobre el error repetido de return/print (E1.1, y ya antes en D1):** 
La primera vez no entendía la diferencia conceptual. Esta vez fue automatismo: seguí escribiendo `print()` por costumbre aunque ya sabía que debía usar `return`. La regla que me llevo: si una función no tiene su propio `print()`, el print va afuera, al llamarla — no adentro de la función. Voy a revisar esto 
específicamente en el próximo ejercicio antes de dar por terminado el código, como un check final antes de entregar.