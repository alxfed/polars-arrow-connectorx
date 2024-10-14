# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
import polars as pl
from timeit import default_timer as timer


def main():
    df = pd.read_csv('/media/alxfed/data1/games/AC/csv/players/played_in_june.csv', parse_dates=[3,4,5,6])
    poldf = pl.from_pandas(df)

    print(poldf.head(5))
    return True


if __name__ == '__main__':
    result = main()
    print(f'main {result}')