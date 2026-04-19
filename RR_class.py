# +----------------------------------------------------------------------------+
# | CARDUI TECH v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2026 - 2026, CARDUITECH.COM (www.carduitech.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.carduitech.com/license/
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: April 11th, 2026
# | Last update..: April 12th, 2026
# | WhatIs.......: Round Robin (RR) - Class
# +----------------------------------------------------------------------------+

# ------------------------- Libraries -------------------------
import pandas as pd
from cmath import isnan

# -------------------------- Imports --------------------------
from ProcessSchedulingVisualizer_class import BaseScheduler

# ------------------------- Class -------------------------
class RRScheduler(BaseScheduler):
    def __init__(self, quantum=2):
        super().__init__()
        self.quantum = quantum
        self.change_process = False

    def schedule(self, verbose=False):
        self.data_import = self.data_import.sort_values(by='arrival_time')
        print(f'i: {self.data_import.to_string(index=False)}') if verbose else None

        time_limit = self.data_import['duration'].sum() + self.data_import.iloc[-1]['arrival_time']

        print(f'time_limit: {time_limit} μs') if verbose else None

        self.data_import['remaining_time'] = None
        self.data_import['quantum_remaining'] = None

        for i in range(0, time_limit + 1):
            print(f'{i} μs') if verbose else None

            arrival_processes = self.data_import[self.data_import['arrival_time'] == i]
            arrival_processes['waiting_time'] = 0
            arrival_processes['remaining_time'] = arrival_processes['duration']
            arrival_processes['quantum_remaining'] = self.quantum

            print(f'a: {arrival_processes.to_string(index=False)}') if verbose else None
            self.data_working = pd.concat([self.data_working, arrival_processes], ignore_index=True)

            print(f'w: {self.data_working.to_string(index=False)}') if verbose else None

            if not self.data_working.empty:
                if self.data_working.iloc[0]['quantum_remaining'] <= 0:
                    print(f'[!] No remaining quantum') if verbose else None
                    print(f'w: {self.data_working.to_string(index=False)}') if verbose else None

                    self.data_working = pd.concat([self.data_working.iloc[1:], self.data_working.iloc[[0]]],
                                                  ignore_index=True)
                    print(f'w: {self.data_working.to_string(index=False)}') if verbose else None

                    self.data_working.at[0, 'quantum_remaining'] = self.quantum

                if isnan(self.data_working.iloc[0]['start_time']):
                    self.data_working.at[0, 'start_time'] = i
                    self.data_working.at[0, 'total_time'] = 0
                else:
                    self.data_working.at[0, 'remaining_time'] -= 1
                    self.data_working.at[0, 'total_time'] += 1

                    self.data_working.at[0, 'quantum_remaining'] -= 1

                for j in self.data_working.index:
                    if isnan(self.data_working.iloc[j]['start_time']):
                        self.data_working.at[j, 'waiting_time'] += 1
                        self.data_working.at[j, 'total_time'] = self.data_working.iloc[j]['waiting_time']

                if self.data_working.iloc[0]['remaining_time'] == 0:
                    self.data_working.at[0, 'end_time'] = i
                    self.data_working.at[0, 'average_time'] = self.data_working.at[0, 'total_time'] / (
                                self.data_working.at[0, 'end_time'] - self.data_working.at[
                            0, 'start_time'])

                    print(
                        f'average_time: {self.data_working.at[0, 'total_time']} / ({self.data_working.at[0, 'end_time']} - {self.data_working.at[
                            0, 'start_time']}) = {self.data_working.at[0, 'average_time']}') if verbose else None
                    print(f'w: {self.data_working.to_string(index=False)}') if verbose else None

                    self.data_export = pd.concat([self.data_export, self.data_working.iloc[:1]], ignore_index=True)
                    self.data_working = self.data_working.drop(self.data_working.index[0]).reset_index(drop=True)

                    self.data_working.at[0, 'start_time'] = i

                print(f'w: {self.data_working.to_string(index=False)}') if verbose else None
                # print(f'i: {self.data_import.to_string(index=False)}') if verbose else None

        print(f'e: {self.data_export.to_string(index=False)}') if verbose else None

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

                waiting = matplotlib.patches.Rectangle((arrival_time, y), start - arrival_time, 1, color=random_rgb,
                                                       fill=False, hatch='/')
                working = matplotlib.patches.Rectangle((start, y), finish - start, 1, color=random_rgb)

                ax.add_patch(waiting)
                ax.add_patch(working)

                rx, ry = working.get_xy()
                cx = rx + working.get_width() / 2.0
                cy = (ry + working.get_height() / 2.0) - 0.05
                ax.annotate(row['process_name'], (cx, cy), color='w', weight='bold', fontsize=10, ha='center',
                            va='center')

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