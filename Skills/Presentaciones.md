# Skill: Generador Diagrama
from graphviz import Digraph

dot = Digraph(comment='Sistema Mental Brayan')
dot.node('A', 'Lóbulo Frontal')
dot.node('B', 'Rueda de Llull')
dot.node('C', 'Inglés')

dot.edges(['AB', 'AC'])
dot.render('diagrama_sistema.gv', view=True)

# Skill: Generador de Documentos .docx

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
