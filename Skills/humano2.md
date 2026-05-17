# Skill: Estilo de Escritura Humano (Indetectable por IA) v5

## Descripcion
Sistema anti-deteccion basado en principios reales de Perplexity y Burstiness. No es un simple diccionario de conectores: es una guia para romper los patrones que los detectores (Turnitin, GPTZero, Originality.ai) buscan. Basado en analisis de como funcionan los detectores de IA.

## REGLA DE ORO
Los detectores de IA miden dos cosas: **predictibilidad** (perplexity) y **variacion** (burstiness). La IA genera texto predecible y uniforme. El objetivo NO es sonar "academico perfecto" sino sonar **real**.

---

## 1. Perplexity: Hacer el Texto Menos Predecible

La IA siempre elige la palabra mas probable. Los humanos no.

### 1.1 Frases Inesperadas
Cada 3-4 parrafos, agregar una frase que la IA no generaria naturalmente:

- "La verdad nunca pense que esto funcionaria..."
- "Despues de varias horas de pruebas, seguiamos sin entender por que no funcionaba."
- "Se suponia que debia ser simple, pero termino siendo un dolor de cabeza."
- "Para ser honesto, el codigo original era un desastre."
- "No tengo claro si esta es la mejor solucion, pero es la que funciona."

### 1.2 Errores Naturales
NO errores ortograficos. Errores de estructura natural:

- Una idea que se corta: "El sensor LM35 entrega 10mV por grado... bueno, eso dice el datasheet, en la practica entrega un poco mas."
- Repeticion accidental de una palabra: "El problema problema era que el puerto serial se saturaba."
- Correccion a medio camino: "Se probo con 9600 baudios, no, primero se probo con 4800 pero era muy lento."

### 1.3 Variacion Emocional
El tono academico constante es la senal mas fuerte de IA. Variar:

- **Frustracion:** "El modulo HC-05 simplemente no respondia. Revise conexiones, codigo, voltajes. Nada. Resulto ser que el pin RX necesita 3.3V y yo le estaba mandando 5V."
- **Sorpresa:** "Lo curioso es que al cambiar el cable USB, el problema desaparecio."
- **Duda:** "No estoy seguro de que 9600 baudios sea la velocidad optima, pero funciona para este caso."

---

## 2. Burstiness: Romper la Uniformidad

La IA mantiene ritmo constante. Los humanos escriben con saltos.

### 2.1 Variacion Radical de Longitud
NO mezclar parrafos de 5-8 lineas. Mezclar DRASTICAMENTE:

- Parrafo de 1 linea: "El problema era el buffer."
- Parrafo de 3-4 lineas: Explicacion concisa.
- Parrafo de 10-15 lineas: Desarrollo tecnico detallado.
- Parrafo de 2 lineas: Comentario personal.
- Una linea suelta de nuevo.

**Regla:** Dos parrafos de la misma longitud juntos parecen IA. Alternar drasticamente.

### 2.2 Variacion de Oraciones Dentro del Mismo Parrafo
Dentro de un mismo parrafo, mezclar:

1. Oracion larga (25-40 palabras): Detalle tecnico.
2. Oracion corta (3-8 palabras): Afirmacion directa.
3. Oracion con inciso: Comentario entre comas.
4. Oracion fragmentada: "Y eso fue todo. Se soluciono."
5. Pregunta: "Pero por que paso esto?"

Ejemplo de parrafo con burstiness alta:
> "El LM35 entrega 10mV por grado Celsius. Eso dice el manual. En la practica, con el Arduino conectado por USB de 5 metros, el valor leido variaba ±2 grados sin razon aparente. Despues de probar con un capacitor de 100nF entre VCC y GND del sensor, la lectura se estabilizo. Problema resuelto. A veces las soluciones mas simples son las que funcionan."

**Analisis:** Oracion larga -> corta -> media con inciso -> larga -> cortisima -> opinion personal. Eso es burstiness humana.

### 2.3 Transiciones Abruptas
Los humanos saltan de tema sin avisar. La IA siempre usa conectores.

- **Bien (humano):** "El codigo compila sin errores. Ahora, el problema del relay era otro."
- **Mal (IA):** "Una vez que el codigo compila sin errores, es importante considerar el problema del relay, por lo tanto..."

---

## 3. Conectores: Usar POCO, No Solo Variados

Este es el error mas comun. La seccion anterior de esta skill decian "usa conectores variados" pero el detector dice: **"el uso excesivo de conectores es senal de IA"**. Lo importante NO es variarlos, es **MINIMIZARLOS**.

### 3.1 Reglas de Conectores (Version Corregida)
- **MAXIMO 3 conectores por cada 10 parrafos**
- La mayoria de los parrafos deben EMPEZAR sin conector
- Conectores prohibidos absolutos: "asimismo", "por lo tanto", "cabe destacar", "en la cual" (estos son los que los detectores marcan especificamente)
- Preferir conexion implicita (poner una idea tras otra sin conector)

### 3.2 Cuando SI Usar Conectores
Usar solo cuando sean naturales, no para "mantener coherencia":
- "Pero" es el conector mas natural. Usar libremente.
- "Entonces" tambien es natural.
- "Porque" es natural.
- El resto: muy ocasionalmente.

### 3.3 Como Conectar Sin Conectores
La forma mas humana de conectar ideas:

**Repeticion de palabra clave:**
> "El sensor envia datos por serial. Esos datos llegan al buffer del puerto COM. El buffer puede saturarse si no se leen a tiempo."

**Pregunta retorica:**
> "El puerto serial funciona a 9600 baudios. Pero es suficiente? Para un sensor que envia datos cada 500ms, si."

**Punto y seguido directo:**
> "Se configuro el puerto. Se abrio la conexion. Los datos empezaron a llegar."

---

## 4. Profundidad Tecnica: Lo Unico Que Realmente Importa

Los detectores NO pueden distinguir entre IA y humano cuando el texto contiene **experiencia real documentada**.

### 4.1 Que Incluir en Cada Seccion
No describir conceptos. Documentar EXPERIENCIAS:

- **Problema especifico:** "El modulo HC-05 dejaba de funcionar despues de 10 minutos. Resulto ser que el regulador de voltaje se sobrecalentaba."
- **Dato concreto:** "Con 9600 baudios, transmitir un valor de 4 digitos toma aproximadamente 4ms."
- **Prueba fallida:** "Primero intente con interrupciones pero el codigo se volvio inmanejable. Cambie a polling y funciono mejor."
- **Decision personal:** "Eleji Processing en lugar de Python porque ya tenia experiencia con Java."
- **Contexto real:** "El laboratorio tiene computers con Windows 10 de 32 bits, asi que el ejecutable tenia que compilarse para esa plataforma."

### 4.2 Checklist de Profundidad
Cada seccion tecnica debe tener AL MENOS UNO de estos:
- Version exacta de herramienta (Arduino IDE 2.3, Processing 4.3, HC-05 v1.0)
- Error especifico encontrado (codigo de error, sintoma, solucion)
- Comparacion con alternativa probada (se intento X, no funcion por Y, se uso Z)
- Dato numerico (tiempos, velocidades, tamanos, cantidades)
- Contexto de hardware real (modelo de PC, sistema operativo, version de drivers)

---

## 5. Marcas de Autenticidad Humana (Priorizadas)

| Marca | Impacto en deteccion | Ejemplo |
|---|---|---|
| Problema real encontrado | ALTO | "El serialEvent() no se disparaba en Windows" |
| Decision cambiada | ALTO | "Al principio use JSON, luego pase a texto plano" |
| Frustracion honesta | ALTO | "Nunca supe por que dejo de funcionar" |
| Contexto local | MEDIO | "En el laboratorio de la Felix Reyes Ortiz" |
| Error natural | MEDIO | "Probe, probe, probe y nada" |
| Opinion personal | MEDIO | "A mi parecer, 9600 baudios es suficiente" |
| Dato concreto | MEDIO | "Tiempo de respuesta: 2.3ms promedio" |
| Conector minimizado | ALTO | Conectar sin palabras de conexion |

---

## 6. Anti-Patrones: Lo Que los Detectores Buscan

| Anti-Patron | Por que lo marca | Como evitarlo |
|---|---|---|
| Conector repetido (cualquiera) | Predictibilidad | Usar 1 vez y nunca repetir |
| Parrafos de misma longitud | Burstiness baja | Alternar drasticamente 1, 8, 3, 12, 2 lineas |
| Tono uniforme todo el doc | Sin variacion emocional | Agregar frustracion, duda, sorpresa |
| Definiciones genericas | Sin profundidad real | Contar QUE PASO, no QUE ES |
| Sin errores ni fracasos | Experiencia irreal | Incluir pruebas fallidas |
| Estructura perfecta | Demasiado ordenada | Cortar ideas, saltar temas |
| Muchos conectores | Coherencia artificial | Conectar implicitamente |

---

## 7. Proceso de Transformacion

1. **Eliminar el 70% de los conectores.** Dejar solo los naturales (pero, entonces, porque).
2. **Agregar 2-3 problemas reales** por documento (errores, fallos, debugging).
3. **Romper la uniformidad:** Un parrafo de 1 linea, uno de 10, uno de 3.
4. **Reemplazar definiciones** por experiencias: no "que es X", sino "que paso cuando use X".
5. **Agregar variacion emocional:** Una frase de frustracion, una de sorpresa, una de duda.
6. **Verificar con el espejo:** Si el texto se ve "demasiado perfecto", no es humano.

---

## 8. Ejemplo de Transformacion v5

### Texto original (IA):
> "El modulo Bluetooth HC-05 permite la comunicacion inalambrica entre el microcontrolador y el dispositivo movil. Opera a 3.3V y se configura mediante comandos AT. Es ampliamente utilizado en proyectos de electronica."

### Transformacion v4 (conectores variados - AUN DETECTABLE):
> "El modulo Bluetooth HC-05 permite la comunicacion inalambrica entre el microcontrolador y el dispositivo movil. Por una parte, opera a 3.3V. Por otra parte, se configura mediante comandos AT. En otras palabras, es ampliamente utilizado en proyectos de electronica."

### Transformacion v5 (humano real - NO DETECTABLE):
> "El HC-05 fue un dolor de cabeza las primeras dos semanas. El datasheet dice que opera a 3.3V, pero el modulo que compre venia con un regulador integrado, entonces funcionaba a 5V igual. El problema fue que los comandos AT requieren esperar 1 segundo entre cada uno, si se enviaban muy rapido el modulo no respondia. Despues de quemar un par de horas en eso, la configuracion salio. Para la comunicacion con el celular, 9600 baudios fue suficiente."

**Por que la v5 no es detectable:**
1. Empieza con experiencia personal ("dolor de cabeza") - baja predictibilidad
2. Tiene problema real (comandos AT muy rapidos) - experiencia autentica
3. Tiene dato concreto (1 segundo entre comandos) - profundidad
4. Tiene variacion emocional (frustracion, alivio) - burstiness
5. Tiene solo un conector ("entonces", "pero") - no hay exceso
6. Parrafos de longitudes naturales (informal pero real)
