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
# | Last update..: April 11th, 2026
# | WhatIs.......: First Come First Serve (FIFO) - Class
# +----------------------------------------------------------------------------+

# ------------------------- Libraries -------------------------
import pandas as pd
from cmath import isnan

# -------------------------- Imports --------------------------
from ProcessSchedulingVisualizer_class import BaseScheduler

# ------------------------- Class -------------------------
class FIFOScheduler(BaseScheduler):
    def __init__(self):
        super().__init__()

    def schedule(self, verbose=False):
        self.data_import = self.data_import.sort_values(by='arrival_time')
        print(f'i: {self.data_import.to_string(index=False)}') if verbose else None

        time_limit = self.data_import['duration'].sum()
        # time_limit = self.data_import[['duration', 'arrival_time']].sum()
        print(f'time_limit: {time_limit} μs') if verbose else None

        self.data_import['remaining_time'] = None

        for i in range(0, time_limit + 1):
            print(f'{i} μs') if verbose else None

            arrival_processes = self.data_import[self.data_import['arrival_time'] == i]
            arrival_processes['waiting_time'] = 0
            arrival_processes['remaining_time'] = arrival_processes['duration']

            print(f'a: {arrival_processes.to_string(index=False)}') if verbose else None
            self.data_working = pd.concat([self.data_working, arrival_processes], ignore_index=True)

            print(f'w: {self.data_working.to_string(index=False)}') if verbose else None

            if not self.data_working.empty:
                if isnan(self.data_working.iloc[0]['start_time']):
                    self.data_working.at[0, 'start_time'] = i
                    self.data_working.at[0, 'total_time'] = 0
                else:
                    self.data_working.at[0, 'remaining_time'] -= 1
                    self.data_working.at[0, 'total_time'] += 1

                for j in self.data_working.index:
                    if isnan(self.data_working.iloc[j]['start_time']):
                        self.data_working.at[j, 'waiting_time'] += 1
                        self.data_working.at[j, 'total_time'] = self.data_working.iloc[j]['waiting_time']

                if self.data_working.iloc[0]['remaining_time'] == 0:
                    self.data_working.at[0, 'end_time'] = i
                    self.data_working.at[0, 'average_time'] = self.data_working.at[0, 'total_time'] / (self.data_working.at[0, 'end_time'] - self.data_working.at[
                        0, 'start_time'])

                    print(f'average_time: {self.data_working.at[0, 'total_time']} / ({self.data_working.at[0, 'end_time']} - {self.data_working.at[
                        0, 'start_time']}) = {self.data_working.at[0, 'average_time']}') if verbose else None
                    print(f'w: {self.data_working.to_string(index=False)}') if verbose else None

                    self.data_export = pd.concat([self.data_export, self.data_working.iloc[:1]], ignore_index=True)
                    self.data_working = self.data_working.drop(self.data_working.index[0]).reset_index(drop=True)

                    self.data_working.at[0, 'start_time'] = i

                print(f'w: {self.data_working.to_string(index=False)}') if verbose else None
                # print(f'i: {self.data_import.to_string(index=False)}') if verbose else None

        print(f'e: {self.data_export.to_string(index=False)}') if verbose else None