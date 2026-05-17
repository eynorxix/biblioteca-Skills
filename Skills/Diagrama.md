# Skill: Generador de Diagramas con Graphviz
> Crea diagramas de nodos personalizados en **SVG** con colores de alto contraste.
> El SVG se puede abrir y editar en **draw.io**.
> Sin tema fijo. Tú defines los nodos y conexiones.

---

## 1. Qué hace

Genera un diagrama de nodos en **SVG** usando Graphviz. Ideal para mapas conceptuales, diagramas de flujo, organigramas, mapas mentales, etc.

El SVG se abre directamente en **draw.io** (editor de diagramas web: https://app.diagrams.net) para editar formas, colores y conexiones.

**No tiene contenido fijo.** Los nodos, colores y conexiones los defines tú.

---

## 2. Instalación Automática

```python
import subprocess, sys, shutil

def instalar_dependencias():
    ok = True
    try:
        import graphviz
        print(f"[OK] graphviz {graphviz.__version__}")
    except ImportError:
        print("[...] Instalando graphviz (Python)...")
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "graphviz",
                 "--break-system-packages"]
            )
            print("[OK] graphviz Python instalado")
        except:
            print("[ERROR] graphviz Python"); ok = False

    if not shutil.which("dot"):
        print("[...] Instalando graphviz (sistema)...")
        try:
            subprocess.check_call(["yay", "-S", "--noconfirm", "graphviz"])
            print("[OK] dot instalado")
        except:
            print("[ERROR] Prueba: yay -S graphviz"); ok = False
    else:
        try:
            ver = subprocess.check_output(["dot", "-V"],
                                          stderr=subprocess.STDOUT).decode().strip()
            print(f"[OK] {ver}")
        except:
            pass
    return ok
```

---

## 3. Paleta de Colores (Alto Contraste)

| Relleno          | Texto    | Razón Técnica                              |
|------------------|----------|---------------------------------------------|
| `#FFFF00` (Amarillo) | Negro    | Máximo contraste percibido                  |
| `#00FF00` (Lima)     | Negro    | El ojo es más sensible a este verde         |
| `#FF0000` (Rojo)     | Blanco   | El rojo oscuro "se come" al negro           |
| `#00008B` (Azul osc) | Blanco   | Evita la fatiga visual                      |
| `#00FFFF` (Cian)     | Negro    | El cian es muy luminoso                     |
| `#FF00FF` (Magenta)  | Blanco   | Equilibrio de luminancia                    |
| `#000000` (Negro)    | Blanco   | Contraste máximo fondo/texto                |
| `#FFFFFF` (Blanco)   | Negro    | Estándar para fondos claros                 |

Uso recomendado: asigna un color por nivel o categoría de nodo.

---

## 4. Código

```python
import subprocess, sys, shutil


def instalar_dependencias():
    ok = True
    try:
        import graphviz
    except ImportError:
        print("[...] Instalando graphviz (Python)...")
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "graphviz",
                 "--break-system-packages"]
            )
        except:
            print("[ERROR] graphviz Python"); ok = False
    if not shutil.which("dot"):
        print("[...] Instalando graphviz (sistema)...")
        try:
            subprocess.check_call(["yay", "-S", "--noconfirm", "graphviz"])
        except:
            print("[ERROR] Prueba: yay -S graphviz"); ok = False
    return ok


# ─────────────────────────────────────────────
# ESTILOS DISPONIBLES
# ─────────────────────────────────────────────

ESTILOS = [
    {
        "nombre": "Minimalista",
        "desc": "Cajas grises finas, sin relleno, bordes sutiles",
        "dir": "TB",
        "bg": "white",
        "node_shape": "box",
        "node_style": "solid",
        "node_color": "#333333",
        "node_fill": "transparent",
        "node_font": "#333333",
        "edge_color": "#666666",
        "edge_width": "0.5",
    },
    {
        "nombre": "Terminal",
        "desc": "Fondo negro, letras verde matrix, fuente Courier",
        "dir": "TB",
        "bg": "#0a0a0a",
        "node_shape": "box",
        "node_style": "filled",
        "node_color": "#00ff41",
        "node_fill": "#0a0a0a",
        "node_font": "#00ff41",
        "edge_color": "#00ff41",
        "edge_width": "0.5",
    },
    {
        "nombre": "Paper",
        "desc": "Fondo sepia, bordes marron, aspecto cuaderno",
        "dir": "TB",
        "bg": "#f5f0e8",
        "node_shape": "box",
        "node_style": "filled",
        "node_color": "#8b7355",
        "node_fill": "#f5f0e8",
        "node_font": "#5c4033",
        "edge_color": "#8b7355",
        "edge_width": "0.5",
    },
    {
        "nombre": "Blueprint",
        "desc": "Fondo azul tecnico, aspecto plano de ingenieria",
        "dir": "TB",
        "bg": "#e8f0f8",
        "node_shape": "box",
        "node_style": "filled",
        "node_color": "#2c5f8a",
        "node_fill": "#d0e0f0",
        "node_font": "#1a3a5c",
        "edge_color": "#2c5f8a",
        "edge_width": "0.6",
    },
    {
        "nombre": "Monocromo",
        "desc": "Blanco y negro puro, sin colores",
        "dir": "TB",
        "bg": "white",
        "node_shape": "box",
        "node_style": "filled",
        "node_color": "#000000",
        "node_fill": "#ffffff",
        "node_font": "#000000",
        "edge_color": "#000000",
        "edge_width": "0.3",
    },
    {
        "nombre": "Flujograma",
        "desc": "Formas clasicas: elipse inicio/fin, rombo decision",
        "dir": "TB",
        "bg": "white",
        "node_shape": "box",
        "node_style": "filled",
        "node_color": "#333333",
        "node_fill": "#f5f5f5",
        "node_font": "#000000",
        "edge_color": "#666666",
        "edge_width": "0.5",
        "shapes_per_node": True,
    },
    {
        "nombre": "Arquitectura",
        "desc": "Horizontal (LR), estilo diagrama de sistemas",
        "dir": "LR",
        "bg": "white",
        "node_shape": "box",
        "node_style": "filled",
        "node_color": "#444444",
        "node_fill": "#fafafa",
        "node_font": "#222222",
        "edge_color": "#888888",
        "edge_width": "0.5",
    },
    {
        "nombre": "Oscuro",
        "desc": "Fondo azul noche, bordes rojo neon",
        "dir": "TB",
        "bg": "#1a1a2e",
        "node_shape": "box",
        "node_style": "filled",
        "node_color": "#e94560",
        "node_fill": "#16213e",
        "node_font": "#ffffff",
        "edge_color": "#e94560",
        "edge_width": "0.5",
    },
]


def generar_diagrama(archivo_salida, nodos, conexiones, estilo_idx,
                     titulo=None):
    """
    Genera un diagrama en SVG usando el estilo indicado.

    Parametros:
        archivo_salida: nombre del SVG
        nodos: lista de dicts {"id","label","fill","font","shape"}
        conexiones: lista de tuples (origen, destino)
        estilo_idx: indice del estilo en ESTILOS
        titulo: texto opcional arriba
    """
    import graphviz
    estilo = ESTILOS[estilo_idx]

    dot = graphviz.Digraph(name="Diagrama", format="svg", engine="dot")
    dot.attr(rankdir=estilo["dir"], splines="ortho", bgcolor=estilo["bg"],
             fontsize="13", fontname="Arial", label=titulo or "", labelloc="t")
    dot.attr("node", fontname="Arial", fontsize="10")

    for nodo in nodos:
        shape = nodo.get("shape", estilo["node_shape"])
        dot.node(nodo["id"], nodo.get("label", nodo["id"]),
                 shape=shape,
                 style=estilo["node_style"],
                 color=estilo["node_color"],
                 fillcolor=nodo.get("fill", estilo["node_fill"]),
                 fontcolor=nodo.get("font", estilo["node_font"]))

    for origen, destino in conexiones:
        dot.edge(origen, destino, color=estilo["edge_color"],
                 penwidth=estilo["edge_width"])

    dot.render(archivo_salida.replace(".svg", ""), cleanup=True)
    print(f"\n[OK] {archivo_salida}")
    print(f"  Estilo: {estilo['nombre']}")
    print(f"  Nodos: {len(nodos)}, Conexiones: {len(conexiones)}")


# ─────────────────────────────────────────────
# DATOS DE EJEMPLO POR ESTILO
# ─────────────────────────────────────────────

def datos_ejemplo(estilo_idx):
    if estilo_idx == 5:  # Flujograma
        nodos = [
            {"id": "start", "label": "Inicio", "fill": "#e0e0e0", "font": "#000", "shape": "ellipse"},
            {"id": "proc",  "label": "Proceso", "fill": "#f5f5f5", "font": "#000", "shape": "box"},
            {"id": "dec",   "label": "Valido?", "fill": "#f5f5f5", "font": "#000", "shape": "diamond"},
            {"id": "ok",    "label": "OK", "fill": "#e8f5e9", "font": "#2e7d32", "shape": "box"},
            {"id": "err",   "label": "Error", "fill": "#ffebee", "font": "#c62828", "shape": "box"},
            {"id": "end",   "label": "Fin", "fill": "#e0e0e0", "font": "#000", "shape": "ellipse"},
        ]
        cones = [("start","proc"),("proc","dec"),("dec","ok"),("dec","err"),("ok","end"),("err","end")]
        return nodos, cones, "Diagrama de Flujo"

    if estilo_idx == 6:  # Arquitectura
        nodos = [
            {"id": "a", "label": "Frontend", "fill": "#fafafa", "font": "#222"},
            {"id": "b", "label": "API",      "fill": "#fafafa", "font": "#222"},
            {"id": "c", "label": "Base Datos","fill": "#fafafa", "font": "#222"},
            {"id": "d", "label": "Cache",    "fill": "#fafafa", "font": "#222"},
        ]
        cones = [("a","b"),("b","c"),("c","d"),("d","a")]
        return nodos, cones, "Arquitectura del Sistema"

    nodos = [
        {"id": "a", "label": "Concepto A", "fill": None, "font": None},
        {"id": "b", "label": "Concepto B", "fill": None, "font": None},
        {"id": "c", "label": "Concepto C", "fill": None, "font": None},
        {"id": "d", "label": "Concepto D", "fill": None, "font": None},
    ]
    cones = [("a","b"),("b","c"),("c","d")]
    return nodos, cones, "Diagrama de Ejemplo"


# ─────────────────────────────────────────────
# MENU INTERACTIVO
# ─────────────────────────────────────────────

def main():
    print()
    print("=" * 50)
    print("  GENERADOR DE DIAGRAMAS GRAPHVIZ")
    print("=" * 50)

    print("\n[1/3] Verificando dependencias...")
    if not instalar_dependencias():
        sys.exit(1)

    # Elegir estilo
    print("\n[2/3] Elige un estilo:")
    print("-" * 50)
    for i, e in enumerate(ESTILOS):
        print(f"  [{i+1}] {e['nombre']:13s} - {e['desc']}")
    print("-" * 50)

    try:
        sel = int(input("  Estilo [1-8]: ").strip())
        if sel < 1 or sel > 8:
            sel = 1
    except:
        sel = 1
    estilo_idx = sel - 1
    estilo = ESTILOS[estilo_idx]
    print(f"\n  -> Seleccionaste: {estilo['nombre']}")

    # Elegir datos
    print("\n  [a] Usar datos de ejemplo")
    print("  [m] Definir manualmente")
    opc = input("  Opcion [a/m]: ").strip().lower()

    nodos, cones, titulo = datos_ejemplo(estilo_idx)

    if opc == "m":
        print("\n  Define nodos (id:Texto separados por coma):")
        entrada = input("  Ej: a:Inicio,b:Proceso,c:Fin: ").strip()
        if entrada:
            nodos = []
            for item in entrada.split(","):
                if ":" in item:
                    parts = item.split(":")
                    nodos.append({"id": parts[0], "label": parts[1],
                                  "fill": None, "font": None})
            print("  Define conexiones (origen-destino separados por coma):")
            entrada2 = input("  Ej: a-b,b-c: ").strip()
            if entrada2:
                cones = []
                for item in entrada2.split(","):
                    if "-" in item:
                        parts = item.split("-")
                        cones.append((parts[0], parts[1]))
            titulo = input("  Titulo del diagrama: ").strip() or "Diagrama"

    # Generar
    print(f"\n[3/3] Generando SVG...")
    import graphviz
    archivo = f"diagrama_{estilo['nombre'].lower()}.svg"

    dot = graphviz.Digraph(name="Diagrama", format="svg", engine="dot")
    dot.attr(rankdir=estilo["dir"], splines="ortho", bgcolor=estilo["bg"],
             fontsize="13", fontname="Arial", label=titulo or "", labelloc="t")
    dot.attr("node", fontname="Arial", fontsize="10")

    for nodo in nodos:
        shape = nodo.get("shape", estilo["node_shape"])
        dot.node(nodo["id"], nodo.get("label", nodo["id"]),
                 shape=shape, style=estilo["node_style"],
                 color=estilo["node_color"],
                 fillcolor=nodo.get("fill") or estilo["node_fill"],
                 fontcolor=nodo.get("font") or estilo["node_font"])

    for origen, destino in cones:
        dot.edge(origen, destino, color=estilo["edge_color"],
                 penwidth=estilo["edge_width"])

    dot.render(archivo.replace(".svg", ""), cleanup=True)
    print(f"\n[OK] {archivo}")
    print(f"  Estilo: {estilo['nombre']}")
    print(f"  Abrelo en: https://app.diagrams.net")
    print("=" * 50)


if __name__ == "__main__":
    main()
```

---

## 5. Cómo usar

1. Define tus nodos en `NODOS`:
   ```python
   {"id": "unico", "label": "Texto visible", "fill": "#FFFF00", "font": "#000000"}
   ```

2. Define tus conexiones en `CONEXIONES`:
   ```python
   ("id_origen", "id_destino")
   ```

3. Ejecuta:
   ```bash
   python3 diagrama.py
   ```

4. Abre el SVG generado en **draw.io**:
   - Ve a https://app.diagrams.net
   - Archivo → Abrir → Selecciona tu `.svg`
   - Edita formas, colores, conexiones libremente

5. O desde otro script:
   ```python
   from diagrama import generar_diagrama
   generar_diagrama("mi_diagrama.svg", mis_nodos, mis_conexiones,
                    titulo="Mi Tema")
   ```

---

## 6. Parámetros de `generar_diagrama`

| Parámetro    | Qué hace                                      |
|-------------|-----------------------------------------------|
| `archivo_salida` | Nombre del SVG (ej: `"diagrama.svg"`)       |
| `nodos`     | Lista de dicts con id, label, fill, font       |
| `conexiones` | Lista de tuples (origen, destino)              |
| `titulo`    | Texto opcional arriba del diagrama             |
| `dir_grafo` | `"TB"` (vertical), `"LR"` (horizontal), `"BT"`, `"RL"` |
| `color_fondo` | Color de fondo (ej: `"white"`, `"#F5F5F5"`) |

---

*Skill genérica de diagramas. Sin tema fijo. Usa la paleta de alto contraste.*
