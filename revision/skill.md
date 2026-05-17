# Skill: Generador de Documentos .docx (UNIFRANZ / APA 7)

## Descripción
Genera documentos `.docx` con precisión quirúrgica para la Universidad Privada Franz Tamayo (UNIFRANZ), utilizando formato APA 7ma edición. El método evita conversiones usando `python-docx` para manipular el XML de Office directamente ("método de dibujo").

## 1. Verificación de Prerrequisitos (Arch Linux)
Antes de generar cualquier documento, verifica que las herramientas necesarias estén instaladas. Ejecuta la verificación en el siguiente orden:

1.  **Verificar Python 3:** `python3 --version`
2.  **Verificar pip:** `pip --version`
3.  **Verificar python-docx:** `python3 -c "import docx"`

### Si algo falta, instruye al usuario para instalarlo:

**Paso A: Instalar pip (si falta)**
> "Para evitar errores 404 en Arch Linux, sincroniza la base de datos primero:"
> ```bash
> sudo pacman -Syu python-pip
> ```

**Paso B: Instalar la librería de documentos**
> ```bash
> pip install python-docx --break-system-packages
> ```
> *Nota: El flag `--break-system-packages` es requerido en Arch Linux moderno para instalaciones fuera de venv.*

## 2. Configuración del Lienzo (Page Setup)
Cada documento debe inicializar una `section` con:
- **Tamaño de papel:** US Letter (8.5 x 11 pulgadas).
- **Márgenes:**
  - Superior: 2.54 cm
  - Inferior: 2.54 cm
  - Derecho: 2.54 cm
  - Izquierdo: 3.0 cm (Encuadernación)

## 3. Definición de Estilos (APA 7)
Redefine el estilo `Normal` y los encabezados:

- **Estilo Normal:**
  - Fuente: Arial, 12pt, Negro.
  - Alineación: Justificada.
  - Interlineado: 1.5 líneas.
  - Sangría primera línea: 1.25 cm.
  - Espaciado antes/después: 0 pt.

- **Título 2 (Heading 2):**
  - Fuente: Arial, 12pt, Negrita, Negro.
  - Alineación: Izquierda.
  - Espaciado antes: 12 pt, después: 6 pt.

- **Título 3 (Heading 3):**
  - Fuente: Arial, 12pt, Negrita + Cursiva, Negro.
  - Alineación: Izquierda.
  - Espaciado antes: 12 pt, después: 6 pt.

*Nota: No se utilizan Títulos de Nivel 1 para el cuerpo del documento, solo para portadas de capítulos si se requieren, pero en este formato general se usan solo Nivel 2 y 3.*

## 4. Estilo de Carátula
La carátula debe contener texto centrado en este orden exacto:
1.  **UNIVERSIDAD PRIVADA FRANZ TAMAYO** (14pt, Negrita)
2.  **SEDE EL ALTO** (14pt, Negrita)
3.  **FACULTAD DE INGENIERIA** (14pt, Negrita)
4.  **CARRERA DE INGENIERIA DE SISTEMAS** (14pt, Negrita)
5.  *(Espacio de 80pt)* **PROYECTO** (12pt, Negrita)
6.  *(Espacio de 20pt)* **Logo UNIFRANZ** (Centrado, Ancho: 7.04 cm, Alto: 6.68 cm)
    - Ruta de la imagen: `/home/eynor/Documentos/Biblioteca/logoUnifranz/logounifranz.png`
    - En `python-docx` usar: `doc.add_picture(ruta, width=Cm(7.04), height=Cm(6.68))` con alineación de párrafo centrada.
7.  *(Espacio de 40pt)* **"TITULO DEL PROYECTO"** (13pt, Negrita)
8.  *(Espacio de 40pt)* Subtítulo/Descripción (12pt, Normal)
9.  *(Espacio de 50pt)* **AUTOR: (Nombre)** (12pt)
10. **TUTOR: (Nombre)** (12pt)
11. *(Espacio de 50pt)* **EL ALTO - BOLIVIA \n 2026** (12pt, Negrita)

## 5. Construcción de Tablas (APA 7)
Las tablas deben generarse manipulando los bordes XML (`w:tcBorders`) para cumplir APA:
- **Encabezado:** Borde superior e inferior (single, size 6).
- **Filas de datos:** Sin bordes verticales ni horizontales internos.
- **Última fila:** Solo borde inferior (single, size 6).
- **Alineación de encabezado:** Centrada.
- **Fuente de tabla:** Arial, 12pt (encabezado), 10pt (cuerpo).
- **Sin sangria izquierdo** justificado el texto de extreo a extremo de cada fila
- **Primera fila** en caso de ser tablas que nombren herramientas o metodos usar la siguiente(nombrar heraminetas primera fila Nombre de las herreminetas), en caso de otras tablas solo usar codigos, solo en requeriminetos funcionales(RF), para requerimeintos no fucnionales(RNF)

## 6. Flujo de Generación
1.  Recibe los datos del usuario (título, autor, contenido, tablas).
2.  Crea un script de Python `generar_documento.py`.
3.  El script sigue estrictamente las reglas de configuración, estilos y tablas.
4.  Ejecuta el script: `python generar_documento.py`.
5.  Entrega el archivo `.docx` resultante.
# Insertar campo TOC funcional (niveles 1-3, hipervínculos, estilos)
p = doc.add_paragraph()
run = p.add_run()
fld_char_begin = parse_xml(
    f'<w:fldChar {nsdecls("w")} w:fldCharType="begin"/>'
)
run._r.append(fld_char_begin)

run2 = p.add_run()
instr_text = parse_xml(
    f'<w:instrText {nsdecls("w")} xml:space="preserve"> TOC \\o "1-3" \\h \\z \\u </w:instrText>'
)
run2._r.append(instr_text)

run3 = p.add_run()
fld_char_separate = parse_xml(
    f'<w:fldChar {nsdecls("w")} w:fldCharType="separate"/>'
)
run3._r.append(fld_char_separate)

run4 = p.add_run()
run4.text = 'Haga clic derecho y seleccione "Actualizar campos" para generar la tabla de contenido.'
run4.font.name = 'Arial'
run4.font.size = Pt(10)
run4.font.italic = True

run5 = p.add_run()
fld_char_end = parse_xml(
    f'<w:fldChar {nsdecls("w")} w:fldCharType="end"/>'
)
run5._r.append(fld_char_end)

doc.add_page_break()
```

### Parámetros del campo TOC:
- `\\o "1-3"`: Incluye niveles de esquema 1, 2 y 3.
- `\\h`: Crea hipervínculos clickeables a cada sección.
- `\\z`: Oculta los números de página y caracteres de tabulación en vista web.
- `\\u`: Usa estilos de párrafo (Heading 1, Heading 2, Heading 3) para construir el índice.

### Requisito para que funcione:
Todos los títulos del documento deben usar los estilos de Word `doc.add_heading(text, level=2)` o `level=3`. No usar párrafos con formato manual para títulos, ya que el campo TOC solo detecta los estilos de encabezado nativos.
