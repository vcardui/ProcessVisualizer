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
# | Last update..: April 11th, 2026
# | WhatIs.......: Process Scheduling Visualizer (Base) - Class
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------
# How to add a text into a Rectangle?: https://stackoverflow.com/questions/14531346/how-to-add-a-text-into-a-rectangle

# ------------------------- Libraries -------------------------
from pathlib import Path # Path().mkdir()
import pandas as pd
import numpy as np

import random
import string

import matplotlib
import matplotlib.pyplot as plt

# ------------------------- Constraints -------------------------
IMPORTS_FOLDER = 'data/'
EXPORTS_FOLDER = 'data/'

empty_record = {
    "process_name": [],
    "arrival_time": [],
    "duration": [],
    "priority": [],
    "start_time": [],
    "end_time": [],
    "total_time": [],
    "waiting_time": [],
    "average_time": []
}

def ask_for_int(question, bad_response='Please enter a positive integer'):
    ok_answer = False
    value = 0

    while not ok_answer:
        value = input(question)
        if value.isdigit():
            ok_answer = True
        else:
            print(bad_response)

    return int(value)

def ask_for_yes_no(question, accepted, not_accepted, bad_response):
    if accepted is None:
        accepted = ['yes', 'Y', 'y', 'Yes', 'YES']

    if not_accepted is None:
        not_accepted = ['no', 'N', 'n', 'No', 'NO']

    ok_answer = False
    value = None

    while not ok_answer:
        value = input(question)
        if value in accepted:
            ok_answer = True
            value = True
        elif value in not_accepted:
            ok_answer = True
            value = False
        else:
            if bad_response:
                print(f'{bad_response} {"/".join(map(str, accepted))} | {"/".join(map(str, not_accepted))}')

    return bool(value)

# ------------------------- Class -------------------------
class BaseScheduler:
    def __init__(self):
        self.data_import = pd.DataFrame()
        self.data_working = pd.DataFrame()
        self.data_export = pd.DataFrame()
        self.file_name = None

    def import_file(self, file_name, show_data=False, show_msg=False):
        try:
            self.data_import = pd.read_csv(IMPORTS_FOLDER + file_name, index_col=False)
            print(self.data_import.to_dict()) if show_msg else None
            print(f"File found ({file_name})") if show_msg else None

        except FileNotFoundError or IndexError:
            print(f'File not found') if show_msg else None
            """
            print(f'File not found. Creating CSV at {IMPORTS_FOLDER}{file_name}')
            Path(f'{IMPORTS_FOLDER}').mkdir(parents=True, exist_ok=True)

            self.data_import = pd.DataFrame(empty_record)
            self.data_import.to_csv(IMPORTS_FOLDER + file_name, index=False)
            print(f"File successfully created ({file_name})") if show_msg else None
            """
        finally:
            print(self.data_import.head()) if show_data else None

    def export_data(self, file_name, show_msg=False):
        if not self.data_export.empty:
            print(f'Creating CSV at {EXPORTS_FOLDER}{file_name}') if show_msg else None
            Path(f'{EXPORTS_FOLDER}').mkdir(parents=True, exist_ok=True)

            self.file_name = file_name

            self.data_export.to_csv(f'{EXPORTS_FOLDER}{file_name}', index=False)
            print(f"File successfully created ({file_name})") if show_msg else None
        else:
            print(f'Empty data to export - File not created')

    def get_user_input_data(self, file_name, verbose=False):
        process_name = []
        arrival_time = []
        duration = []
        priority = []

        new = True
        i = 1
        max_items = 100
        while new:
            print(f'\nProceso #{i}')

            process_name.append(input('Nombre del proceso: '))
            arrival_time.append(ask_for_int('Tiempo de llegada (μs): ', 'Por favor ingrese un número entero positivo'))
            duration.append(ask_for_int('Duración (μs): ', 'Por favor ingrese un número entero'))
            priority.append(ask_for_int('Prioridad: ', 'Por favor ingrese un número entero'))

            i += 1
            new = ask_for_yes_no('¿Desea ingresar un nuevo elemento?: ',
                                 accepted=['yes', 'Y', 'y', 'Yes', 'YES', 'si', 's', 'S', 'SI', 'sí', 'SÍ'],
                                 not_accepted=['no', 'N', 'n', 'No', 'NO'],
                                 bad_response='[!] Respuesta no válida\nPor favor ingrese: ')

        data = pd.DataFrame(columns=['process_name', 'arrival_time', 'duration', 'priority', 'start_time', 'end_time', 'total_time', 'waiting_time', 'average_time'])
        data['process_name'] = process_name
        data['arrival_time'] = arrival_time
        data['duration'] = duration
        data['priority'] = priority

        print(data) if verbose else None

        data.to_csv(IMPORTS_FOLDER + file_name, index=False)

    def get_random_data(self, file_name, items=20, verbose=False):
        process_name = []
        arrival_time = []
        duration = []
        priority = []

        for i in range(0, items + 1):
            process_name.append(string.ascii_uppercase[i])
            arrival_time.append(random.randint(1, 20))
            duration.append(random.randint(1, 10))
            priority.append(random.randint(1, 5))

        data = pd.DataFrame(columns=['process_name', 'arrival_time', 'duration', 'priority', 'start_time', 'end_time', 'total_time', 'waiting_time', 'average_time'])
        data['process_name'] = process_name
        data['arrival_time'] = arrival_time
        data['duration'] = duration
        data['priority'] = priority

        print(data) if verbose else None

        data.to_csv(IMPORTS_FOLDER + file_name, index=False)

    def schedule(self, verbose=False):
        pass

    def render(self, show_msg=False):
        end_time = int(self.data_export['end_time'].iloc[-1])
        print(f"end_time: {end_time}") if show_msg else None

        n_processes = int(len(self.data_export.index))
        print(f"n_processes: {n_processes}") if show_msg else None

        fig = plt.figure(figsize=(14, 7))
        ax = fig.add_subplot(111)

        y = 0
        for index, row in self.data_export.iterrows():
            random_rgb = np.random.rand(3)

            arrival_time = row['arrival_time']
            start = row['start_time']
            finish = row['end_time']

            print(f'arrival_time: {arrival_time}, start: {start}, finish: {finish}') if show_msg else None

            waiting = matplotlib.patches.Rectangle((arrival_time, y), start - arrival_time, 1, color=random_rgb, fill=False, hatch='/')
            working = matplotlib.patches.Rectangle((start, y), finish - start, 1, color=random_rgb)

            ax.add_patch(waiting)
            ax.add_patch(working)

            rx, ry = working.get_xy()
            cx = rx + working.get_width() / 2.0
            cy = (ry + working.get_height() / 2.0) - 0.05
            ax.annotate(row['process_name'], (cx, cy), color='w', weight='bold', fontsize=10, ha='center', va='center')

            y += 1

        for j in range(0, end_time):
            if j % 10 == 0:
                plt.axvline(x=j, color='gray', linestyle='--')
            elif j % 2 == 0:
                plt.axvline(x=j, color='gray', linestyle=':')

        plt.xlim([0, end_time])
        plt.ylim([0, n_processes])

        ax.set_title(f'{self.file_name} - FIFO')
        ax.set_xlabel("Tiempo μs")
        ax.set_ylabel("N° de proceso")

        plt.show()