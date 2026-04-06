# +----------------------------------------------------------------------------+
# | CARDUI TECH v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2026 - 2026, CARDUITECH.COM (www.carduitech.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.carduitech.com/license/
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: April 4th, 2026
# | Last update..: April 4th, 2026
# | WhatIs.......: Process Visualizer - Main
# +-----------------------------------------------------------------------------+
# ------------------------- Instructions ----------------------
"""
Desarrolla un menú con 3 opciones, dos de las opciones debe de ser de Algoritmo
de procesos, la tercera opción puede ser Algoritmos de procesos o Remplazo de
páginas, de las posibles mostradas a continuación:

**Algoritmos de Procesos**

- Tabla de procesos FIFO (incluir tabla y gráfica)
- Tabla de procesos Round Robin (incluir tabla y gráfica)
- Tablas de procesos por el trabajo más corto primero (incluir tabla y gráfica)

**Algoritmo de reemplazo de páginas**

- Tabla de reemplazo de páginas la menos recientemente utilizada
- Tabla de reemplazo de páginas FIFO

La gráfica puede ser en el formato que se desee.

Desarrollar en el lenguaje de programación de su elección.

El programa permite seleccionar al usuario cuantos procesos o cuantas páginas
despachara , además debe de tener 2 opciones de llenado:

- llenado de datos por los usuarios
- llenado aleatorio por parte del sistema

Puede ser en equipo de 3 personas, pero c/u realiza su entrega en el
Aula virtual y en equipo en presencial.

La entrega en Aula debe de ser el programa, y un documento , con pequeña
explicación de algoritmos seleccionados, conclusiones individuales por
lo menos 200 palabras por personas.
"""

# ------------ Resources / Documentation involved -------------
# ------------------------- Libraries -------------------------

# -------------------------- Imports --------------------------
from FIFO_class import FIFOScheduler

# -------------------------- Objects --------------------------
FIFO = FIFOScheduler()
FIFO.import_data("test.csv")
FIFO.schedule(verbose=True)
FIFO.export_data("test_export.csv")

# ------------------------- Variables -------------------------

# --------------------------- Code ----------------------------