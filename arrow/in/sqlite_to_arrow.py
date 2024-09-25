# -*- coding: utf-8 -*-
"""...
"""
import connectorx as cx
import pyarrow as pa
import polars as pl

s = pl.threadpool_size()
conn = "sqlite:///media/alxfed/data1/games/AC/sqlite/airport_quests.sqlite"
tables = ['']
query = """
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
    FROM payment_august_installs"""

table = cx.read_sql(conn, query, return_type="arrow")

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
table = table.cast(right_schema)

df = pl.from_arrow(table)
# df.drop_in_place(name="event_data")
# df.drop_in_place(name="offer_id")

pdf = df.to_pandas()

print('ok')
