from threading import Thread
from StatisticsByRegion import StatisticsByRegion

import os
import time
import json
import pandas as pd


class ThreadStats(Thread):
    def __init__(self):
        self.pathToData = "data/"
        Thread.__init__(self)

    def run(self):
        while True:
            files = os.listdir(self.pathToData)
            for file in files:
                filepath = self.pathToData + file
                filewithoutextension = os.path.splitext(file)[0]
                if time.time() - os.path.getmtime(filepath) > 12*60*60:
                    statistics = StatisticsByRegion("all", filewithoutextension)
                    df = statistics.getStats()
                    if isinstance(df, pd.DataFrame):
                        df.reset_index(inplace=True, drop=True)
                        df = df.to_dict(orient='index')
                    with open(filepath, 'w') as f:
                        json.dump(df, f)
                    print("Stats of the file %s updated" % file)
            time.sleep(60)
