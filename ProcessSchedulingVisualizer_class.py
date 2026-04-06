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
# | WhatIs.......: Process Scheduling Visualizer (Base) - Class
# +----------------------------------------------------------------------------+

# ------------------------- Libraries -------------------------
from pathlib import Path # Path().mkdir()
import pandas as pd

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
        self.data_import = None
        self.data_working = None
        self.data_export = None

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

        self.data_export = pd.DataFrame.from_records(self.data_working)
        self.data_export.to_csv(f'{EXPORTS_FOLDER}{file_name}', index=False)
        print(f"File successfully created ({file_name})") if show_msg else None

    def schedule(self, verbose=False):
        pass