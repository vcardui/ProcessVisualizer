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
# | Last update..: April 5th, 2026
# | WhatIs.......: First Come First Serve (FIFO) - Class
# +----------------------------------------------------------------------------+

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

        for i in range(0, time_limit + 1):
            print(f'{i} μs') if verbose else None

            """
            if not queue:
                queue.append(self.data_working[0])
                self.data_working.pop(0)

                queue[0]['start_time'] = i
                queue[0]['remaining_time'] = queue[0]['duration']

            else:
                if queue[0]['remaining_time'] == 0:

                    queue.pop(0)
                else:
                    queue[0]['remaining_time'] = queue[0]['remaining_time'] - 1
            """

            print(f'w: {self.data_working}') if verbose else None
            print(f'q: {queue}') if verbose else None

        print(f'f: {self.data_export}') if verbose else None