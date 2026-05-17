import math
import subprocess
import sys

def instalar_reportlab():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
        return True
    except:
        pass
    try:
        subprocess.check_call(["yay", "-S", "--noconfirm", "python-reportlab"])
        return True
    except:
        pass
    return False

try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
except ImportError:
    if not instalar_reportlab():
        print("[ERROR] No se pudo instalar reportlab.")
        sys.exit(1)
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors


def dibujar_anillo(c, anillo, cx, cy):
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

    c.setFillColor(colors.black)
    c.circle(cx, cy, 2, stroke=0, fill=1)


def generar_ruedas_separadas(nombre_archivo, anillos):
    c = canvas.Canvas(nombre_archivo, pagesize=A4)
    cx, cy = A4[0] / 2, A4[1] / 2

    # Pagina 1: anillo 1 (negro, exterior) solo
    dibujar_anillo(c, anillos[0], cx, cy)

    # Pagina 2: anillo 2 (azul) solo
    c.showPage()
    dibujar_anillo(c, anillos[1], cx, cy)

    # Pagina 3: anillo 3 (rojo) + anillo 4 (verde) lado a lado
    c.showPage()
    cx_izq = A4[0] * 0.28
    cx_der = A4[0] * 0.72
    dibujar_anillo(c, anillos[2], cx_izq, cy)
    dibujar_anillo(c, anillos[3], cx_der, cy)

    c.save()
    print(f"[OK] {nombre_archivo}")


ANILLOS = [
    {"ext": 250, "int": 195, "seg": 12, "color": colors.black},
    {"ext": 185, "int": 135, "seg": 12, "color": colors.blue},
    {"ext": 125, "int": 80,  "seg": 12, "color": colors.red},
    {"ext": 70,  "int": 30,  "seg": 12, "color": colors.green},
]

ARCHIVO_SALIDA = "/home/eynor/Documentos/Biblioteca/rueda/Ruedas_por_anillo.pdf"

if __name__ == "__main__":
    print("=" * 45)
    print("Rueda de Llull - 4 anillos en paginas separadas")
    print("=" * 45)
    print("  Pagina 1: Anillo 1 (negro, exterior) solo")
    print("  Pagina 2: Anillo 2 (azul) solo")
    print("  Pagina 3: Anillos 3 (rojo) + 4 (verde) lado a lado")
    print(f"\n[OK] Generando {ARCHIVO_SALIDA}...")
    generar_ruedas_separadas(ARCHIVO_SALIDA, ANILLOS)
    print(f"\n  Listo. Revisa {ARCHIVO_SALIDA}")
    print("=" * 45)
