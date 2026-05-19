# Guía del Desarrollador

## Arquitectura del Sistema

```
base_documento.py    →   Motor de formato APA (reutilizable)
EstructuraIntegrador.md →  Plantilla de estructura del Integrador (opcional)
generar_TEMA.py      →   Script con el contenido específico
```

---

## 1. Estructura de `base_documento.py`

### Funciones de Configuración Inicial

```python
from base_documento import *

doc = crear_documento()       # Crea documento con márgenes APA
configurar_estilos(doc)       # Aplica estilos Normal, Heading 2, Heading 3
```

### Funciones de Formato APA

| Función | Qué hace | Parámetros clave |
|---------|----------|------------------|
| `crear_documento()` | Crea documento con márgenes APA (21.59x27.94cm, márgenes 2.54/3.0cm) | Ninguno |
| `configurar_estilos(doc)` | Configura Normal (Arial 12, justificado, 1.5), Heading 2 (negrita), Heading 3 (negrita+cursiva) | `doc` |
| `agregar_caratula(doc, titulo, autor, tutor)` | Genera carátula UNIFRANZ con logo | `titulo`, `autor`, `tutor` |
| `agregar_toc(doc)` | Inserta índice automático (TOC) | `doc` |
| `agregar_pagina_capitulo(doc, numero)` | Página fantasma "CAPÍTULO X" tamaño 46 | `numero`: "I", "II", etc. |
| `agregar_nueva_seccion(doc, fmt, start, mostrar)` | Nueva sección con numeración específica | `fmt`: "decimal", "upperRoman" `start`: número inicial `mostrar`: True/False |
| `agregar_referencias(doc, refs)` | Bibliografía con sangría francesa | `refs`: lista de strings APA |

### Funciones de Contenido

| Función | Qué hace | Parámetros clave |
|---------|----------|------------------|
| `add_paragraph(doc, text, bold, size, alignment, ...)` | Añade párrafo con formato APA | `text`, `bold`, `size`, `alignment`, `first_line_indent` |
| `add_heading_custom(doc, text, level)` | Añade título con fuente Arial | `text`, `level`: 2 o 3 |
| `add_bullets(doc, items)` | Lista con viñetas | `items`: lista de strings |
| `add_table_with_data(doc, headers, data, col_alignments, title, note)` | Tabla con bordes APA | Ver sección Tablas |

---

## 2. Cómo Crear un Nuevo Documento (`generar_TEMA.py`)

### Paso 1: Crear el archivo

```python
from base_documento import *

doc = crear_documento()
configurar_estilos(doc)

TITLE = "Título de tu Proyecto"
AUTHOR = "Tu Nombre"
TUTOR = "M.Sc. Nombre del Tutor"
```

### Paso 2: Agregar carátula e índice

```python
configurar_header(doc, doc.sections[0], mostrar=False)
agregar_caratula(doc, TITLE, AUTHOR, TUTOR)

agregar_nueva_seccion(doc, fmt='upperRoman', start=1, mostrar=True)
agregar_toc(doc)
```

### Paso 3: Cada Capítulo

```python
agregar_nueva_seccion(doc, fmt='decimal', start=1, mostrar=True)

# Página fantasma del capítulo
agregar_pagina_capitulo(doc, 'I')
doc.add_page_break()

# Contenido
add_heading_custom(doc, '1. Introducción', level=3)
add_paragraph(doc, 'Texto del párrafo...')

add_heading_custom(doc, '1.1. Antecedentes', level=3)
add_paragraph(doc, 'Texto con cita (Apellido, 2024)...')

add_bullets(doc, ['Primer punto', 'Segundo punto'])
```

### Paso 4: Tablas

```python
add_table_with_data(doc,
    headers=['COLUMNA 1', 'COLUMNA 2'],
    data=[
        ['Fila 1', 'Dato 1'],
        ['Fila 2', 'Dato 2'],
    ],
    col_alignments=[
        WD_ALIGN_PARAGRAPH.LEFT,
        WD_ALIGN_PARAGRAPH.CENTER,
    ],
    title='*Tabla 1. Título de la Tabla*',
    note='Nota: Elaboración propia.'
)
```

### Paso 5: Bibliografía

```python
agregar_referencias(doc, [
    'Apellido, N. (2024). Título del libro. Editorial.',
    'Apellido2, N. (2023). Artículo. Revista, 1(2), 10-20.',
])
```

### Paso 6: Guardar

```python
OUTPUT = '/home/eynor/Documentos/biblioteca-integrador/Informe_TEMA.docx'
doc.save(OUTPUT)
print(f'Documento generado: {OUTPUT}')
```

---

## 3. Cómo Modificar la Carátula

Para cambiar la universidad, facultad o carrera, editar `agregar_caratula()` en `base_documento.py`:

```python
def agregar_caratula(doc, titulo, autor, tutor, logo_path="..."):
    # Cambia estos textos:
    add_paragraph(doc, "UNIVERSIDAD PRIVADA FRANZ TAMAYO", ...)  # Línea 220
    add_paragraph(doc, "SEDE EL ALTO", ...)                       # Línea 221
    add_paragraph(doc, "FACULTAD DE INGENIERIA", ...)             # Línea 222
    add_paragraph(doc, "CARRERA DE INGENIERIA DE SISTEMAS", ...)  # Línea 223
```

Para cambiar el año (2026), modificar la última línea de la carátula:
```python
add_paragraph(doc, "EL ALTO - BOLIVIA\n2026", ...)  # Línea 235
```

Para cambiar la ruta del logo, modificar el parámetro `logo_path`:
```python
logo_path="/home/eynor/Documentos/Biblioteca/logoUnifranz/logounifranz.png"
```

---

## 4. Cómo Cambiar los Estilos APA

En `configurar_estilos()`:

```python
# Fuente (cambiar Arial por Times New Roman, Calibri, etc.)
style.font.name = 'Arial'          # Línea 22
style.font.size = Pt(12)           # Línea 23

# Interlineado (cambiar 1.5 por 2.0, 1.15, etc.)
pf.line_spacing = 1.5              # Línea 27

# Sangría (cambiar 1.25 cm por 0, 0.5, etc.)
pf.first_line_indent = Cm(1.25)    # Línea 28
```

---

## 5. Cómo Crear un Archivo `.md` de Estructura Personalizado

El `EstructuraIntegrador.md` define qué capítulos y secciones debe tener tu documento. Puedes crear tus propios `.md` para diferentes materias.

### Ejemplo: `Estructura_Informe_Tecnico.md`

```markdown
# Skill: Informe Técnico (Formato APA)

## Estructura del Documento

### Portada
- Título del informe
- Autor, Tutor, Fecha

### Resumen Ejecutivo
- Máximo 250 palabras
- Sin citas

### Capítulo I: Descripción del Problema
| Sección | Contenido |
|---------|-----------|
| 1. Introducción | Contexto del problema técnico |
| 1.1. Situación Actual | Diagnóstico inicial |
| 1.2. Requerimientos | Lista de necesidades técnicas |

### Capítulo II: Solución Propuesta
| Sección | Contenido |
|---------|-----------|
| 2. Introducción | Descripción general |
| 2.1. Arquitectura | Diagrama y componentes |
| 2.2. Implementación | Pasos y tecnologías |

### Capítulo III: Resultados
| Sección | Contenido |
|---------|-----------|
| 3. Introducción | Métricas de evaluación |
| 3.1. Pruebas | Resultados obtenidos |
| 3.2. Conclusiones | Logros y limitaciones |

### Anexos
- Código fuente, diagramas, manuales

### Bibliografía
- Formato APA
```

### Reglas para crear un `.md` de estructura

1. **Define las secciones** con tablas de dos columnas (Sección | Contenido)
2. **Especifica el nivel de heading**: Heading 2 para títulos principales, Heading 3 para subsecciones
3. **Indica el tipo de contenido**: texto, tabla, lista con viñetas, cita APA
4. **Numeración**: Sigue el patrón `X. Título`, `X.Y. Subtítulo`, `X.Y.Z. Sub-subtítulo`

---

## 6. Ejemplo Completo Mínimo

```python
from base_documento import *

doc = crear_documento()
configurar_estilos(doc)

configurar_header(doc, doc.sections[0], mostrar=False)
agregar_caratula(doc, "Mi Título", "Mi Nombre", "Mi Tutor")

agregar_nueva_seccion(doc, fmt='upperRoman', start=1, mostrar=True)
agregar_toc(doc)
doc.add_page_break()

agregar_nueva_seccion(doc, fmt='decimal', start=1, mostrar=True)

agregar_pagina_capitulo(doc, 'I')
doc.add_page_break()
add_heading_custom(doc, '1. Introducción', level=3)
add_paragraph(doc, 'Contenido del capítulo...')

agregar_referencias(doc, ['Autor, N. (2024). Obra. Editorial.'])

OUTPUT = '/home/eynor/Documentos/biblioteca-integrador/Mi_Informe.docx'
doc.save(OUTPUT)
print(f'Documento generado: {OUTPUT}')
```

---

## 7. Referencia Rápida de Parámetros

### `add_paragraph(doc, text, ...)`
| Parámetro | Valores posibles | Default |
|-----------|-----------------|---------|
| `bold` | True, False | False |
| `size` | 9, 10, 12, 13, 14, 46 | 12 |
| `alignment` | `WD_ALIGN_PARAGRAPH.CENTER`, `LEFT`, `RIGHT`, `JUSTIFY` | JUSTIFY |
| `space_before` | 0-45 | 0 |
| `space_after` | 0-45 | 0 |
| `first_line_indent` | 0, 1.25, etc. (cm) | 1.25 |
| `italic` | True, False | False |

### `add_table_with_data(doc, ...)`
| Parámetro | Descripción |
|-----------|-------------|
| `headers` | Lista de strings para encabezados |
| `data` | Lista de listas con filas |
| `col_alignments` | Lista de `WD_ALIGN_PARAGRAPH.*` por columna |
| `title` | String con título arriba de la tabla |
| `note` | String con nota al pie debajo de la tabla |

### `agregar_nueva_seccion(doc, ...)`
| Parámetro | Descripción |
|-----------|-------------|
| `fmt` | `"decimal"` (1,2,3), `"upperRoman"` (I,II,III) |
| `start` | Número inicial de página |
| `mostrar` | True (visible), False (oculto) |
