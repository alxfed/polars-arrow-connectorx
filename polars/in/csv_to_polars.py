# -*- coding: utf-8 -*-
"""...
"""
import polars as pl
from timeit import default_timer as timer


def main():
    file_name = 'app_players'
    # https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.read_csv.html
    try:
        start = timer()
        poldf = pl.read_csv(f'/media/alxfed/data1/games/AC/csv/players/{file_name}.csv',
                            try_parse_dates=True,
                            # use_pyarrow=True,
                            n_threads=8)
        end = timer()
        # print(f'time spent {end-start} \n')
    except Exception as ex:
        print(f'There was a {ex} exception')
        poldf = pl.DataFrame()
        return False

    print(poldf.head(5))

    # https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.DataFrame.write_parquet.html
    try:
        start = timer()
        poldf.write_parquet(f'/media/alxfed/data/games/AC/parquet/{file_name}.parquet',
                            use_pyarrow=True
                            )
        end = timer()
        print(f'time spent {end - start} \n')
    except Exception as ex:
        print(f'There was a {ex} exception')
        return False

    # https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.read_parquet.html
    # https://arrow.apache.org/docs/python/generated/pyarrow.parquet.read_table.html
    try:
        start = timer()
        poldf = pl.read_parquet(f'/media/alxfed/data/games/AC/parquet/{file_name}.parquet',
                                use_pyarrow=True,
                                parallel='auto'
                                )
        end = timer()
        print(f'time spent {end - start} \n')
    except Exception as ex:
        print(f'There was a {ex} exception')
        return False

    return True


if __name__ == '__main__':
    result = main()
    print(f'main {result}')