# +----------------------------------------------------------------------------+
# | CARDUI TECH v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2026 - 2026, CARDUITECH.COM (www.carduitech.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.carduitech.com/license/
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: April 5th, 2026
# | Last update..: April 8th, 2026
# | WhatIs.......: First Come First Serve (FIFO) - Class
# +----------------------------------------------------------------------------+
from cmath import isnan

# ------------------------- Libraries -------------------------
import pandas as pd

# -------------------------- Imports --------------------------
from ProcessSchedulingVisualizer_class import BaseScheduler

# ------------------------- Class -------------------------
class FIFOScheduler(BaseScheduler):
    def __init__(self):
        super().__init__()

    def schedule(self, verbose=False):
        time_limit = self.data_import['duration'].max() + self.data_import['arrival_time'].max()
        print(f'time_limit: {time_limit} μs') if verbose else None

        self.data_import['remaining_time'] = None
        # self.data_import = self.data_import.to_dict("records")

        # self.data_working = pd.DataFrame()

        for i in range(0, time_limit + 1):
            print(f'{i} μs') if verbose else None

            arrival_processes = self.data_import[self.data_import['arrival_time'] == i]
            arrival_processes['waiting_time'] = 0
            arrival_processes['remaining_time'] = arrival_processes['duration']

            self.data_working = pd.concat([self.data_working, arrival_processes], ignore_index=True)

            if isnan(self.data_working.iloc[0]['start_time']):
                self.data_working.at[0, 'start_time'] = i
                self.data_working.at[0, 'total_time'] = 0
            else:
                self.data_working.at[0, 'remaining_time'] -= 1
                self.data_working.at[0, 'total_time'] += 1

            for j in self.data_working.index:
                if j !=0:
                    print(f"j: {j}")
                    self.data_working.at[j, 'total_time'] += 1

                    if self.data_working.iloc[j]['start_time'] == 0:
                        self.data_working.at[j, 'waiting_time'] += 1

            if self.data_working.iloc[0]['remaining_time'] == 0:
                self.data_working.at[0, 'end_time'] = i
                self.data_working.at[0, 'average_time'] = (self.data_working.at[0, 'end_time'] - self.data_working.at[
                    0, 'start_time']) / self.data_working.at[0, 'total_time']

                print(f'w: {self.data_working.to_string(index=False)}') if verbose else None

                self.data_export = pd.concat([self.data_export, self.data_working.iloc[:1]], ignore_index=True)
                self.data_working = self.data_working.drop(self.data_working.index[0]).reset_index(drop=True)

                self.data_working.at[0, 'start_time'] = i
                self.data_working.at[0, 'total_time'] = 0

            print(f'w: {self.data_working.to_string(index=False)}') if verbose else None
            # print(f'i: {self.data_import.to_string(index=False)}') if verbose else None

        print(f'e: {self.data_export.to_string(index=False)}') if verbose else None