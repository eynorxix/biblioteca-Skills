# Generador de Ruedas Concéntricas
> Skill genérica para generar N anillos con M segmentos cada uno
> Sin tema fijo — solo la estructura mecánica de las ruedas

---

## 1. Qué hace

Genera un PDF con **N anillos concéntricos**. Cada anillo es una corona circular con **M segmentos**. Soporta dos modos:

- **Modo A** (original): todos los anillos concéntricos en una sola página
- **Modo B** (páginas separadas): cada anillo en su propia página, con opción de poner anillos pequeños lado a lado para ahorrar espacio

Sin contenido temático — solo la estructura de las ruedas. Sin números de texto a menos que se configuren.

---

## 2. Instalación Automática

Si `reportlab` no está instalado, lo instala por `pip` o `yay`.

---

## 3. Código

```python
import math
import subprocess
import sys


# ─────────────────────────────────────────────
# INSTALACIÓN AUTOMÁTICA
# ─────────────────────────────────────────────

def instalar_reportlab():
    print("[...] Instalando reportlab...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
        print("[OK] via pip")
        return True
    except:
        pass
    try:
        subprocess.check_call(["yay", "-S", "--noconfirm", "python-reportlab"])
        print("[OK] via yay")
        return True
    except:
        pass
    print("[ERROR] No se pudo instalar reportlab.")
    return False


def verificar_sistema():
    try:
        import reportlab
        print(f"[OK] reportlab {reportlab.Version}")
        return True
    except ImportError:
        return instalar_reportlab()


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


# ─────────────────────────────────────────────
# GENERADOR DE RUEDAS
# ─────────────────────────────────────────────

def dibujar_anillo(c, anillo, cx, cy, con_texto=False):
    """
    Dibuja un solo anillo en (cx, cy).
    anillo: {"ext": ..., "int": ..., "seg": ..., "color": ...}
    Si con_texto=True, muestra el numero de segmento.
    """
    ext = anillo["ext"]
    inter = anillo["int"]
    color = anillo["color"]
    num_seg = anillo["seg"]

    c.setStrokeColor(color)
    c.setLineWidth(1)
    c.circle(cx, cy, ext, stroke=1, fill=0)
    c.circle(cx, cy, inter, stroke=1, fill=0)

    ang_paso = 360.0 / num_seg
    for i in range(num_seg):
        ang_div = i * ang_paso
        rd = math.radians(ang_div)

        c.setDash(1, 2)
        c.setStrokeColor(color)
        c.line(
            cx + inter * math.cos(rd), cy + inter * math.sin(rd),
            cx + ext * math.cos(rd), cy + ext * math.sin(rd)
        )

        if con_texto:
            texto = str(i + 1)
            ang_medio = ang_div + (ang_paso / 2)
            r_texto = (ext + inter) / 2
            r_ajuste = r_texto - 5

            c.setDash()
            c.saveState()

            rt = math.radians(ang_medio)
            tx = cx + r_ajuste * math.cos(rt)
            ty = cy + r_ajuste * math.sin(rt)

            rot = ang_medio - 90
            a = ang_medio % 360
            if 90 < a < 270:
                rot += 180

            c.translate(tx, ty)
            c.rotate(rot)
            c.setFont("Helvetica-Bold", 8)
            c.setFillColor(colors.black)
            c.drawCentredString(0, 0, texto)
            c.restoreState()

    c.setFillColor(colors.black)
    c.circle(cx, cy, 2, stroke=0, fill=1)


# ── Modo A: todos los anillos concentricos en una pagina ──

def generar_ruedas_concentricas(nombre_archivo, anillos, con_texto=False):
    c = canvas.Canvas(nombre_archivo, pagesize=A4)
    cx, cy = A4[0] / 2, A4[1] / 2

    for anillo in anillos:
        dibujar_anillo(c, anillo, cx, cy, con_texto)

    c.save()
    print(f"[OK] {nombre_archivo}")


# ── Modo B: anillos en paginas separadas ──

def generar_ruedas_por_pagina(nombre_archivo, anillos,
                              independientes=None, lado_a_lado=None):
    """
    anillos: lista completa de anillos
    independientes: lista de indices que van solos en su pagina
    lado_a_lado: lista de indices que van juntos lado a lado
      ej: independientes=[0,1], lado_a_lado=[2,3]
    """
    c = canvas.Canvas(nombre_archivo, pagesize=A4)
    cy = A4[1] / 2

    for i, idx in enumerate(independientes):
        if i > 0:
            c.showPage()
        dibujar_anillo(c, anillos[idx], A4[0] / 2, cy)

    if lado_a_lado:
        c.showPage()
        n = len(lado_a_lado)
        for j, idx in enumerate(lado_a_lado):
            cx = A4[0] * (j + 1) / (n + 1)
            dibujar_anillo(c, anillos[idx], cx, cy)

    c.save()
    print(f"[OK] {nombre_archivo}")


# ─────────────────────────────────────────────
# CONFIGURACIÓN
# ─────────────────────────────────────────────

ANILLOS = [
    {"ext": 250, "int": 195, "seg": 12, "color": colors.black},
    {"ext": 185, "int": 135, "seg": 12, "color": colors.blue},
    {"ext": 125, "int": 80,  "seg": 12, "color": colors.red},
    {"ext": 70,  "int": 30,  "seg": 12, "color": colors.green},
]

# ── Elegir modo ──
# Opcion A: todos concentricos en una pagina
# Opcion B: cada anillo en su propia pagina

MODO = "B"  # Cambiar a "A" para el modo concentrico clasico

# Para modo B: definir que anillos van solos y cuales lado a lado
#   - independientes: indices que ocupan pagina entera
#   - lado_a_lado: indices que se reparten la misma pagina
INDEPENDIENTES = [0, 1]   # anillos 1 y 2 (negro, azul) cada uno su pagina
LADO_A_LADO = [2, 3]      # anillos 3 y 4 (rojo, verde) lado a lado

CON_TEXTO = False          # True para mostrar numeros de segmento

ARCHIVO_SALIDA = "/home/eynor/Documentos/Biblioteca/rueda/Ruedas.pdf"


# ─────────────────────────────────────────────
# EJECUCIÓN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 45)
    print("Generador de Ruedas Concentricas")
    print("=" * 45)

    print("\n[1/2] Verificando dependencias...")
    if not verificar_sistema():
        sys.exit(1)

    print(f"\nAnillos: {len(ANILLOS)}")
    for i, a in enumerate(ANILLOS):
        print(f"  Anillo {i+1}: ext={a['ext']}, int={a['int']}, seg={a['seg']}")

    print(f"\n[2/2] Modo {MODO}...")
    if MODO == "A":
        generar_ruedas_concentricas(ARCHIVO_SALIDA, ANILLOS, CON_TEXTO)
    elif MODO == "B":
        generar_ruedas_por_pagina(ARCHIVO_SALIDA, ANILLOS,
                                  INDEPENDIENTES, LADO_A_LADO)
    else:
        print("[ERROR] MODO debe ser 'A' o 'B'")
        sys.exit(1)

    print(f"\n  Listo. Revisa {ARCHIVO_SALIDA}")
    print("=" * 45)
```

---

## 4. Cómo configurar

Edita las variables en la sección `CONFIGURACIÓN`:

```python
ANILLOS = [
    {"ext": 250, "int": 195, "seg": 12, "color": colors.black},
    {"ext": 185, "int": 135, "seg": 12, "color": colors.blue},
    {"ext": 125, "int": 80,  "seg": 12, "color": colors.red},
    {"ext": 70,  "int": 30,  "seg": 12, "color": colors.green},
]

MODO = "B"
INDEPENDIENTES = [0, 1]
LADO_A_LADO = [2, 3]
CON_TEXTO = False
```

| Variable | Qué hace |
|----------|----------|
| `ext` | Radio exterior del anillo (puntos) |
| `int` | Radio interior del anillo (puntos) |
| `seg` | Número de segmentos en que se divide |
| `color` | Color del borde del anillo |
| `MODO` | `"A"` = todos concéntricos, `"B"` = páginas separadas |
| `INDEPENDIENTES` | Índices de anillos que van solos en su página (modo B) |
| `LADO_A_LADO` | Índices de anillos que comparten página lado a lado (modo B) |
| `CON_TEXTO` | `True` para mostrar números de segmento, `False` para solo estructura |

Los gaps entre `int` de un anillo y `ext` del siguiente deben ser ≥ 5 pt para que giren libres.

Todos los anillos deben tener el mismo número de segmentos (`seg`) para que las divisiones queden alineadas radialmente entre sí.

---

## 5. Notas

- Sin tema fijo. Genera solo la estructura de las ruedas.
- Modo A: todos los anillos concéntricos en una sola página (clásico).
- Modo B: controlas qué anillos van en páginas independientes y cuáles van lado a lado para ahorrar espacio.
- Los índices en `INDEPENDIENTES` y `LADO_A_LADO` corresponden a la posición en la lista `ANILLOS` (0 = primero).
- Los radios se calculan para A4 (máximo ~280 pt antes de salir de la página).
- Todos los archivos generados (PDF, .py, etc.) se guardan en `/home/eynor/Documentos/Biblioteca/rueda/`

---

*Skill generadora de ruedas concéntricas. Sin contenido temático.*
