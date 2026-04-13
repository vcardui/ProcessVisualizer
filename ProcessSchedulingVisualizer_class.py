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

# ------------------------- Libraries -------------------------
from pathlib import Path # Path().mkdir()
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

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

# ------------------------- Class -------------------------
class BaseScheduler:
    def __init__(self):
        self.data_import = pd.DataFrame()
        self.data_working = pd.DataFrame()
        self.data_export = pd.DataFrame()

    def import_data(self, file_name, show_data=False, show_msg=False):
        try:
            self.data_import = pd.read_csv(IMPORTS_FOLDER + file_name, index_col=False)
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
        print(f'Creating CSV at {EXPORTS_FOLDER}{file_name}') if show_msg else None
        Path(f'{EXPORTS_FOLDER}').mkdir(parents=True, exist_ok=True)

        self.data_export.to_csv(f'{EXPORTS_FOLDER}{file_name}', index=False)
        print(f"File successfully created ({file_name})") if show_msg else None

    def schedule(self, verbose=False):
        pass

    def render(self, show_msg=False):
        end_time = int(self.data_export['end_time'].iloc[-1])
        print(f"end_time: {end_time}") if show_msg else None

        n_processes = int(len(self.data_export.index))
        print(f"n_processes: {n_processes}") if show_msg else None

        fig = plt.figure(figsize=(10, 5))
        ax = fig.add_subplot(111)

        x = 0
        y = 0
        for i in self.data_export.index:
            random_rgb = np.random.rand(3)

            rect = matplotlib.patches.Rectangle((x, y), 2, 1, color=random_rgb)
            ax.add_patch(rect)
            x += 2
            y += 1

        for j in range(0, end_time):
            if j % 10 == 0:
                plt.axvline(x=j, color='gray', linestyle='--')

        plt.xlim([0, end_time])
        plt.ylim([0, n_processes])

        plt.show()
