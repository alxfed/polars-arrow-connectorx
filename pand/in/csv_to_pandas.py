# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
from timeit import default_timer as timer


start = timer()
df = pd.read_csv('/media/alxfed/data1/games/AC/csv/players/played_in_june.csv')
end = timer()
print(f'pandas read time {end-start}')
print('ok')
