from threading import Thread
from StatisticsByRegion import StatisticsByRegion

import os
import time
import json


class ThreadStatsDZ(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        FILENAME = "dzStats.json"
        while True:
            if time.time() - os.path.getmtime(FILENAME) > 12*60*60:
                statistics = StatisticsByRegion("Dark-Zone")
                df = statistics.getStats()
                df.reset_index(inplace=True, drop=True)
                result = df.to_dict(orient='index')
                with open(FILENAME, 'w') as f:
                    json.dump(result, f)
                print("DZ Stats Updated")
            time.sleep(60)


