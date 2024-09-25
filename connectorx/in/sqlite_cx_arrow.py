# -*- coding: utf-8 -*-
""" Through connectorx into Arrow with a .cast() and on to polars and pandas.
"""
from typing import List, AnyStr
from timeit import default_timer as deftimer
import connectorx as cx
import pyarrow as pa
from pyarrow import Table
import polars as pl


# Configuration of the source(s)
conn = "sqlite:///media/alxfed/data1/games/AC/sqlite/airport_payments.sqlite"
sqlite_db_tables = [
    'payment_june_installs',
    'payment_july',
    'payment_august_installs',
    'payment_september_installs',
    'payment_october_installs'
]

right_schema = pa.schema(
    [
        ("event_id", pa.string()),
        ("uid", pa.string()),
        ("project", pa.string()),
        ("timestamp", pa.timestamp(unit='ms')),
        ("exp", pa.int64()),
        ("sid", pa.int64()),
        ("hard", pa.int64()),
        ("soft", pa.int64()),
        ("level", pa.int64()),
        # ("event_data", pa.string()),
        ("currency", pa.string()),
        # ("inapp_id", pa.string()),
        # ("offer_id", pa.string()),
        ("price_usd", pa.float32()),
        ("value_hard", pa.int64()),
        ("value_soft", pa.int64())
        # ("value_other", pa.string())
    ]
)


def query(table) -> AnyStr:
    query_text = f"""
        SELECT
            event_id,
            uid,
            project,
            timestamp,
            exp,
            sid,
            hard,
            soft,
            level,
            currency,
            price_usd,
            value_hard,
            value_soft
        FROM {table}"""
    return query_text


queries = [query(table) for table in sqlite_db_tables]


def sqlite_cx_arrow(connection:str, queries:List[AnyStr]) -> Table:
    """ Read the set of sqlite tables and return as one Arrow table
    :param connection: conn
    :param queries:
    :return: table
    """
    try:
        start = deftimer()
        arrow_table = cx.read_sql(conn, queries, return_type="arrow")
        arrow_table = arrow_table.cast(right_schema)
        stop = deftimer()
        print(f"Time spent {stop-start}")
        podf = pl.from_arrow(arrow_table)
        padf = podf.to_pandas()
    except Exception as ex:
        print(f"Exception {ex}")
        empty = pa.Table.from_pylist([0], mapping={'a':0})
        return empty

    return arrow_table

# df.drop_in_place(name="event_data")
# df.drop_in_place(name="offer_id")


if __name__ == '__main__':
    arrow_table = sqlite_cx_arrow(conn, queries)
    print('ok')
