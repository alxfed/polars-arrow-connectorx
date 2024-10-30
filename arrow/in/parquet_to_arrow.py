# -*- coding: utf-8 -*-
"""...
"""
from pyarrow.parquet import read_table, read_pandas, read_schema, read_metadata
from timeit import default_timer as timer


def main():

    # https://arrow.apache.org/docs/python/generated/pyarrow.parquet.read_table.html
    try:
        start = timer()
        taf = read_table('/media/alxfed/toca/aws-data-science/airport/parquette.parquet')
        end = timer()
        print(f'time_reading {end-start}')
    except Exception as ex:
        print(f'There was a {ex} exception')
        return False

    return True


if __name__ == '__main__':
    result = main()
    print(f'main: {result}')