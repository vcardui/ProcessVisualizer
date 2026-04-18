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


# -------------------------- Imports --------------------------
from FIFO_class import FIFOScheduler
from RR_class import RRScheduler
from SPN_class import SPNScheduler

# ------------------------ Constraints ------------------------
QUANTUM = 2

# -------------------------- Objects --------------------------
FIFO = FIFOScheduler()
SPN = SPNScheduler()
RR = RRScheduler(QUANTUM)

# --------------------------- Code ----------------------------
"""
# First Come First Serve (FIFO) -> Input
import_filename = 'FIFO_demo_3.csv'
export_filename = 'FIFO_demo_3_export.csv'

# FIFO.get_random_data(import_filename, items=10, verbose=False)
# FIFO.get_user_input_data(import_filename)
FIFO.import_file(import_filename, show_msg=True, show_data=True)
FIFO.schedule(verbose=True)
FIFO.export_data(export_filename)
FIFO.render(show_msg=True)
"""


"""
# First Come First Serve (FIFO) -> Loaded
FIFO.import_file("FIFO_demo.csv")
FIFO.schedule(verbose=True)
FIFO.export_data("FIFO_demo_export.csv")
FIFO.render(show_msg=True)
"""

"""
# Shortest Process Next (SPN)
SPN.import_file("SPN_demo.csv")
SPN.schedule(verbose=True)
SPN.export_data("SPN_demo_export.csv")
SPN.render(show_msg=True)
"""

"""
# Round Robin (RR)
RR.import_file("RR_demo.csv")
RR.schedule(verbose=True)
RR.export_data("RR_demo_export.csv")
RR.render(show_msg=True)
"""

# Round Robin 2 (RR)
RR.import_file("RR2_demo.csv")
RR.schedule(verbose=True)
RR.export_data("RR2_demo_export.csv")
RR.render(show_msg=True)