from threading import Thread
from StatisticsByRegion import StatisticsByRegion

import os
import time
import json


class RetrieveRegionalTweets(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        FILENAME = "regionalStats.json"
        while True:
            if time.time() - os.path.getmtime(FILENAME) > 35:
                statistics = StatisticsByRegion("all")
                df = statistics.getStats()
                df.reset_index(inplace=True, drop=True)
                result = df.to_dict(orient='index')
                with open(FILENAME, 'w') as f:
                    json.dump(result, f)
                print("Regional Stats Updated")
                time.sleep(30)


