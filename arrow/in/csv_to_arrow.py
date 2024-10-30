# -*- coding: utf-8 -*-
"""...
"""
from pyarrow.csv import ReadOptions, ParseOptions, ConvertOptions, read_csv
from timeit import default_timer as timer


def main():
    # https://arrow.apache.org/docs/python/generated/pyarrow.csv.ReadOptions.html
    options = ReadOptions(
            use_threads=True,
            encoding='utf8',
        )

    # https://arrow.apache.org/docs/python/generated/pyarrow.csv.ParseOptions.html
    parse = ParseOptions(
        )

    # https://arrow.apache.org/docs/python/generated/pyarrow.csv.ConvertOptions.html
    convert = ConvertOptions(
        timestamp_parsers=["%m/%d/%Y", "%m-%d-%Y"]
    )

    # https://arrow.apache.org/docs/python/generated/pyarrow.csv.read_csv.html
    try:
        start = timer()
        daf = read_csv('/media/alxfed/toca/aws-data-science/airport/session_202210170725.csv',
                       read_options=options,
                       parse_options=parse,
                       convert_options=convert)
        end = timer()
        print(f'time_reading {end-start}')
    except Exception as ex:
        print(f'There was a {ex} exception')
        return False
    return True


if __name__ == '__main__':
    result = main()
    print(f'main: {result}')