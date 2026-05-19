# Skill: Generador de Documentos .docx (UNIFRANZ / APA 7)

## Descripción
Genera documentos `.docx` con precisión quirúrgica para la Universidad Privada Franz Tamayo (UNIFRANZ), utilizando formato APA 7ma edición. El método evita conversiones usando `python-docx` para manipular el XML de Office directamente ("método de dibujo").

---

## 1. Verificación de Prerrequisitos

```bash
python3 --version
pip --version
python3 -c "import docx"
```

Si falta `python-docx`:
```bash
pip install python-docx --break-system-packages
```

---

## 2. Configuración del Lienzo (Page Setup)

```python
for section in doc.sections:
    section.page_width = Cm(21.59)       # US Letter
    section.page_height = Cm(27.94)
    section.top_margin = Cm(2.54)
    section.bottom_margin = Cm(2.54)
    section.left_margin = Cm(3.0)        # Encuadernación
    section.right_margin = Cm(2.54)
```

---

## 3. Definición de Estilos (APA 7)

### Estilo Normal
- Fuente: Arial, 12pt, Negro.
- Alineación: Justificada.
- Interlineado: 1.5 líneas.
- Sangría primera línea: 1.25 cm.
- Espaciado antes/después: 0 pt.

```python
style = doc.styles['Normal']
style.font.name = 'Arial'
style.font.size = Pt(12)
style.font.color.rgb = RGBColor(0, 0, 0)
pf = style.paragraph_format
pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
pf.line_spacing = 1.5
pf.first_line_indent = Cm(1.25)
pf.space_before = Pt(0)
pf.space_after = Pt(0)
```

### Heading 2 (Título 2)
- Arial, 12pt, **Negrita**, **sin cursiva**, Negro.
- Alineación: Izquierda.
- **Sin sangría**.
- Espaciado antes: 12 pt, después: 6 pt.

### Heading 3 (Título 3) — es el SUBTÍTULO del Título 2
- Arial, 12pt, **Negrita + Cursiva**, Negro.
- Alineación: Izquierda.
- **Sangría izquierda de 1.25 cm**.
- Espaciado antes: 12 pt, después: 6 pt.

```python
hs2 = doc.styles['Heading 2']
hs2.font.name = 'Arial'
hs2.font.size = Pt(12)
hs2.font.color.rgb = RGBColor(0, 0, 0)
hs2.font.bold = True
hs2.font.italic = False
hs2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
hs2.paragraph_format.space_before = Pt(12)
hs2.paragraph_format.space_after = Pt(6)
hs2.paragraph_format.first_line_indent = Cm(0)

hs3 = doc.styles['Heading 3']
hs3.font.name = 'Arial'
hs3.font.size = Pt(12)
hs3.font.color.rgb = RGBColor(0, 0, 0)
hs3.font.bold = True
hs3.font.italic = True
hs3.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
hs3.paragraph_format.space_before = Pt(12)
hs3.paragraph_format.space_after = Pt(6)
hs3.paragraph_format.first_line_indent = Cm(1.25)
```

**Nota:** No se usan Heading 1 en el cuerpo del documento. Solo en páginas individuales de capítulos, y como párrafo normal, no como heading.

---

## 4. GENERAR CARÁTULA

Orden exacto (centrado):

1. **UNIVERSIDAD PRIVADA FRANZ TAMAYO** (14pt, Negrita)
2. **SEDE EL ALTO** (14pt, Negrita)
3. **FACULTAD DE INGENIERIA** (14pt, Negrita)
4. **CARRERA DE INGENIERIA DE SISTEMAS** (14pt, Negrita)
5. *(Espacio 10pt)* **PROYECTO** (12pt, Negrita)
6. *(Espacio 10pt)* **Logo UNIFRANZ** (Centrado, Ancho: 7.04 cm, Alto: 6.68 cm)
   - Ruta: `/home/eynor/Documentos/Biblioteca/logoUnifranz/logounifranz.png`
7. *(Espacio 35pt)* **"TITULO DEL PROYECTO"** (13pt, Negrita)
8. *(Espacio 35pt)* Subtítulo/Descripción (12pt, Normal) — *opcional*
9. *(Espacio 45pt)* **AUTOR: (Nombre)** (12pt)
10. **TUTOR: (Nombre)** (12pt)
11. *(Espacio 45pt)* **EL ALTO - BOLIVIA \n 2026** (12pt, Negrita)

Salto de página después de la carátula.

---

## 5. NUMERACIÓN DE PÁGINAS

### Reglas de numeración

| Sección | Estilo | Visible | Ubicación |
|---------|--------|---------|-----------|
| Carátula | - | No | - |
| Índice / TOC | Romano (i, ii, iii...) | Sí | Esquina superior derecha |
| Capítulo I (página individual) | - | No | "Página fantasma" |
| Capítulo I (contenido) → Capítulo V | Arábigo (1, 2, 3...) | Sí | Esquina superior derecha |
| Anexos / Bibliografía | Arábigo | No | Sin número |

### Explicación de "Numeración Fantasma"
Cada capítulo tiene una **página individual** con solo `CAPÍTULO X` centrado, tamaño **46pt**, sin subtítulo. Esa página NO muestra numeración. La página siguiente (contenido) SÍ muestra numeración CONTINUANDO la secuencia.

```
EJEMPLO:
- Página i: Índice (romano, visible)
- Página ii: Índice continúa (romano, visible)
- [CAPÍTULO I - página individual, sin número, solo "CAPÍTULO I" centrado tamaño 46]
- Página 2: Contenido (arábigo "2", visible) → empieza con "1. Introducción"
- Página 3: Contenido (arábigo "3", visible)
- [CAPÍTULO II - página individual, sin número, solo "CAPÍTULO II" centrado tamaño 46]
- Página 5: Contenido (arábigo "5", visible) → empieza con "2. Introducción"
```

### Implementación en python-docx

```python
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.text import WD_ALIGN_PARAGRAPH

def configurar_header(doc, section, fmt='decimal', start=None, mostrar=True):
    section.different_first_page_header_footer = True
    header = section.header
    header.is_linked_to_previous = False
    if not mostrar:
        return
    for p in header.paragraphs:
        p.clear()
    p = header.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p.paragraph_format.first_line_indent = Cm(0)
    run = p.add_run()
    run.font.name = 'Arial'
    run.font.size = Pt(10)
    # PAGE field XML...
    sectPr = section._sectPr
    pgNumType = OxmlElement('w:pgNumType')
    pgNumType.set(qn('w:fmt'), fmt)
    if start is not None:
        pgNumType.set(qn('w:start'), str(start))
    sectPr.append(pgNumType)
```

**Secciones del documento:**
- **Sección 1:** Carátula → sin numeración
- **Sección 2:** Índice → numeración romana (`upperRoman`), empezando en I
- **Sección 3:** Capítulos I a V → numeración arábiga (`decimal`), empezando en 1
- **Sección 4:** Anexos → sin numeración

---

## 6. PÁGINA FANTASMA DE CADA CAPÍTULO

NO usar Heading 1. Es un párrafo normal centrado con tamaño 46.

```python
def agregar_pagina_capitulo(doc, numero):
    for _ in range(6):
        doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run(f'CAPÍTULO {numero}')
    run.font.name = 'Arial'
    run.font.size = Pt(46)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0)
```

**Secuencia por capítulo:**
```python
# Primer capítulo (después del salto de sección, sin page_break extra):
agregar_pagina_capitulo(doc, 'I')  # Página fantasma solo con "CAPÍTULO I"
doc.add_page_break()               # Salto a contenido

add_heading_custom(doc, '1. Introducción', level=3)  # Contenido empieza aquí

# Capítulos siguientes:
doc.add_page_break()               # Salto de página anterior
agregar_pagina_capitulo(doc, 'II') # Página fantasma
doc.add_page_break()               # Salto a contenido
add_heading_custom(doc, '2. Introducción', level=3)
```

---

## 7. ESTRUCTURA DE CAPÍTULOS Y SUBTÍTULOS

**Regla general:** Todo capítulo empieza con `X. Introducción` (Heading 3, sin ".1"). La numeración del contenido sigue el número del capítulo.

### Capítulo I: Generalidades

| Sección | Nivel | Tipo de contenido |
|---------|-------|-------------------|
| 1. Introducción | Heading 3 | Párrafos de contexto, sin citas |
| 1.1. Antecedentes | Heading 3 | Con citas APA al final de cada párrafo |
| 1.1.1. Antecedentes Internacionales | Heading 3 | Proyectos de otros países |
| 1.1.2. Antecedentes Nacionales | Heading 3 | Proyectos del mismo país |
| 1.1.3. Antecedentes Locales | Heading 3 | Proyectos de la misma ciudad/empresa |
| 1.2. Planteamiento del Problema | Heading 3 | Texto descriptivo, crítico |
| 1.2.1. Identificación de la Situación Problémica | Heading 3 | Situación actual, deficiencias |
| 1.2.2. Formulación del Problema | Heading 3 | Pregunta central: "¿Cómo...?" |
| 1.2.3. Problemas Específicos | Heading 3 | Lista con viñetas |
| 1.3. Objetivos | Heading 3 | |
| 1.3.1. Objetivo General | Heading 3 | Un verbo fuerte: Implementar, Desarrollar |
| 1.3.2. Objetivos Específicos | Heading 3 | Lista con viñetas, orden lógico |
| 1.4. Justificación | Heading 3 | |
| 1.4.1. Justificación Técnica | Heading 3 | Recursos tecnológicos, viabilidad |
| 1.4.2. Justificación Económica | Heading 3 | Costos, retorno de inversión |
| 1.4.3. Justificación Social | Heading 3 | Beneficios a la comunidad |
| 1.5. Alcances y Límites | Heading 3 | |
| 1.5.1. Alcance | Heading 3 | Lo que SÍ hará el proyecto |
| 1.5.2. Límites | Heading 3 | Lo que NO hará el proyecto |

### Capítulo II: Marco Teórico

| Sección | Contenido |
|---------|-----------|
| 2. Introducción | Párrafo introductorio del capítulo (sin cita) |
| 2.1. Concepto 1 | Definición formal + cita + aplicación al proyecto |
| 2.2. Concepto 2 | Definición formal + cita + aplicación al proyecto |
| 2.N. Metodología de Desarrollo | Scrum, UML, etc. |

### Capítulo III: Marco Metodológico

| Sección | Contenido |
|---------|-----------|
| 3. Introducción | Párrafo introductorio del capítulo |
| 3.1. Enfoque de Investigación | Cuantitativo, Cualitativo o Mixto |
| 3.2. Tipo de Investigación | Descriptiva, Exploratoria, Aplicada |
| 3.3. Métodos, Técnicas e Instrumentos | Entrevistas, encuestas, revisión documental |

### Capítulo IV: Marco Práctico

| Sección | Contenido |
|---------|-----------|
| 4. Introducción | Párrafo introductorio del capítulo |
| 4.1. Análisis de Requerimientos | Tablas de RF y RNF |
| 4.2. Arquitectura del Sistema | Diagramas, diseño técnico |

### Capítulo V: Conclusiones y Recomendaciones

| Sección | Contenido |
|---------|-----------|
| 5. Introducción | Párrafo introductorio del capítulo |
| 5.1. Conclusiones | Responden a objetivos específicos, tiempo pasado |
| 5.2. Recomendaciones | Acciones a futuro, tiempo futuro |

---

## 8. FORMATO DE TABLAS

### Reglas generales
- **Título:** ARRIBA, alineado a la izquierda, negrita + cursiva, tamaño 10. Ej: `*Tabla 1. Título*`
- **Encabezados:** MAYÚSCULAS, negrita, centrados.
- **Cuerpo:** Tamaño 10, sin sangría, alineación según contenido.
- **Nota al pie:** Debajo, cursiva, tamaño 9. Ej: `Nota: Elaboración propia...`

### Tipos de columnas
| Tipo | Alineación |
|------|------------|
| ID, Prioridad, Riesgo | Centrado |
| Usuario, Título, Descripción | Izquierda |

---

## 9. FORMATO DE LISTAS CON VIÑETAS

```python
for b in items:
    p = doc.add_paragraph()
    run = p.add_run(f'  \u2022  {b}')
    run.font.name = 'Arial'
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(0, 0, 0)
    p.paragraph_format.first_line_indent = Cm(1.25)
    p.paragraph_format.line_spacing = 1.5
```

---

## 10. FORMATO DE REFERENCIAS (BIBLIOGRAFÍA APA)

```python
for ref in referencias:
    p = doc.add_paragraph()
    run = p.add_run(ref)
    run.font.name = 'Arial'
    run.font.size = Pt(12)
    p.paragraph_format.left_indent = Cm(1.25)
    p.paragraph_format.first_line_indent = Cm(-1.25)  # Sangría francesa
    p.paragraph_format.line_spacing = 1.5
```

---

## 11. FUNCIONES AUXILIARES ESENCIALES

```python
def add_paragraph(doc, text, bold=False, size=12, alignment=None, space_before=0, space_after=0, first_line_indent=None, italic=False):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = RGBColor(0, 0, 0)
    if alignment:
        p.alignment = alignment
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    if first_line_indent is not None:
        p.paragraph_format.first_line_indent = Cm(first_line_indent)
    else:
        p.paragraph_format.first_line_indent = Cm(1.25)
    p.paragraph_format.line_spacing = 1.5
    return p

def add_heading_custom(doc, text, level=2):
    p = doc.add_heading(text, level=level)
    for run in p.runs:
        run.font.name = 'Arial'
        run.font.color.rgb = RGBColor(0, 0, 0)
    return p
```

---

## 12. TOC (Índice automático)

```python
p_toc = doc.add_paragraph()
run_toc = p_toc.add_run()
fld_begin = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="begin"/>')
run_toc._r.append(fld_begin)
run_toc2 = p_toc.add_run()
instr = parse_xml(f'<w:instrText {nsdecls("w")} xml:space="preserve"> TOC \\o "1-3" \\h \\z \\u </w:instrText>')
run_toc2._r.append(instr)
run_toc3 = p_toc.add_run()
fld_sep = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="separate"/>')
run_toc3._r.append(fld_sep)
run_toc4 = p_toc.add_run()
run_toc4.text = '[Click derecho y seleccione "Actualizar campos" para generar el índice]'
run_toc4.font.name = 'Arial'
run_toc4.font.size = Pt(10)
run_toc4.font.italic = True
run_toc5 = p_toc.add_run()
fld_end = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="end"/>')
run_toc5._r.append(fld_end)
```

---

## 13. ESTRUCTURA GENERAL DEL DOCUMENTO

```
PORTADA (1 página, sin numeración)
  ↓
ÍNDICE / TOC (numeración romana: i, ii, iii...)
  ↓
[CAPÍTULO I - página individual: solo "CAPÍTULO I" centrado tamaño 46, sin número]
  ↓
1. Introducción ← contenido empieza aquí
1.1. Antecedentes (1.1.1, 1.1.2, 1.1.3)
1.2. Planteamiento del Problema (1.2.1, 1.2.2, 1.2.3)
1.3. Objetivos (1.3.1, 1.3.2)
1.4. Justificación (1.4.1, 1.4.2, 1.4.3)
1.5. Alcances y Límites (1.5.1, 1.5.2)
  ↓
[CAPÍTULO II - página individual: solo "CAPÍTULO II" centrado tamaño 46, sin número]
  ↓
2. Introducción
2.1. Concepto 1
2.2. Concepto 2
...
  ↓
[CAPÍTULO III - página individual]
  ↓
3. Introducción
3.1. ...
  ↓
[CAPÍTULO IV - página individual]
  ↓
4. Introducción
4.1. ...
  ↓
[CAPÍTULO V - página individual]
  ↓
5. Introducción
5.1. Conclusiones
5.2. Recomendaciones
  ↓
ANEXOS (sin numeración)
  ↓
BIBLIOGRAFÍA (Formato APA)
```

---

## 14. CONVENCIONES DE ESCRITURA

- **Voz:** Activa ("El sistema genera..." no "Es generado por...").
- **Persona:** Se evita "Yo" y "Nosotros". Usar "El presente proyecto", "El autor", "Se desarrolló".
- **Tiempos verbales:**
  - Antecedentes / Marco Teórico: Presente o pasado.
  - Propuesta: Presente.
  - Conclusiones: Pasado.
- **Conectores:** "Asimismo", "De igual manera", "Por otra parte", "En cuanto a", "Sin embargo".
- **Citas:** Al final del párrafo: (Apellido, Año, p. XX). En introducción y conclusiones NO van citas.

---

## 15. DIAGRAMA DE FLUJO DE GENERACIÓN

```
1. Configurar página (márgenes, tamaño Letter)
2. Definir estilos (Normal, Heading 2, Heading 3)
3. Generar CARÁTULA (Sección 1, sin numeración)
4. Generar ÍNDICE / TOC (Sección 2, numeración romana desde I)
5. Para cada CAPÍTULO (I a V) dentro de Sección 3 (arábigo desde 1):
   a. Primer capítulo: solo página fantasma (sin page_break extra)
   b. Capítulos siguientes: page_break + página fantasma
   c. Agregar "X. Introducción" (Heading 3, el primero no lleva ".1")
6. Generar ANEXOS (Sección 4, sin numeración)
7. Generar BIBLIOGRAFÍA
8. Guardar documento
```

---

## 16. SECCIONES DEL DOCUMENTO (IMPLEMENTACIÓN)

```python
# --- Sección 1: Carátula (sin numeración) ---
configurar_header(doc, doc.sections[0], mostrar=False)
agregar_caratula(doc, TITLE, AUTHOR, TUTOR)

# --- Sección 2: Índice (numeración romana) ---
agregar_nueva_seccion(doc, fmt='upperRoman', start=1, mostrar=True)
agregar_toc(doc)

# --- Sección 3: Capítulos I-V (numeración arábiga) ---
agregar_nueva_seccion(doc, fmt='decimal', start=1, mostrar=True)

# Capítulo I
agregar_pagina_capitulo(doc, 'I')
doc.add_page_break()
add_heading_custom(doc, '1. Introducción', level=3)
# ... contenido ...

# Capítulo II
doc.add_page_break()
agregar_pagina_capitulo(doc, 'II')
doc.add_page_break()
add_heading_custom(doc, '2. Introducción', level=3)
# ... contenido ...

# ... (III, IV, V igual) ...

# --- Sección 4: Anexos (sin numeración) ---
agregar_nueva_seccion(doc, mostrar=False)
# ... anexos ...

# --- Bibliografía ---
agregar_referencias(doc, referencias)
```
