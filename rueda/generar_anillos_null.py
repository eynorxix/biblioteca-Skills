import math
import subprocess
import sys

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

def generar_ruedas(nombre_archivo, anillos):
    c = canvas.Canvas(nombre_archivo, pagesize=A4)
    cx, cy = A4[0] / 2, A4[1] / 2

    for anillo in anillos:
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
    c.save()
    print(f"[OK] {nombre_archivo}")

ANILLOS = [
    {"ext": 250, "int": 195, "seg": 12, "color": colors.black},
    {"ext": 185, "int": 135, "seg": 12, "color": colors.blue},
    {"ext": 125, "int": 80,  "seg": 12, "color": colors.red},
    {"ext": 70,  "int": 30,  "seg": 12, "color": colors.green},
]

ARCHIVO_SALIDA = "/home/eynor/Documentos/Biblioteca/rueda/Anillos_Null.pdf"

if __name__ == "__main__":
    print("=" * 45)
    print("Generador de Anillos Null")
    print("=" * 45)

    print("\n[1/2] Verificando dependencias...")
    if not verificar_sistema():
        sys.exit(1)

    print(f"\nAnillos a generar: {len(ANILLOS)}")
    for i, a in enumerate(ANILLOS):
        gap_a = f" (gap {ANILLOS[i-1]['int']-a['ext']} pt)" if i > 0 else ""
        print(f"  Anillo {i+1}: ext={a['ext']}, int={a['int']}, seg={a['seg']}{gap_a}")

    print(f"\n[2/2] Generando {ARCHIVO_SALIDA}...")
    generar_ruedas(ARCHIVO_SALIDA, ANILLOS)

    print(f"\n  Listo. Revisa {ARCHIVO_SALIDA}")
    print("=" * 45)
