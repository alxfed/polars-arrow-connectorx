# -*- coding: utf-8 -*-
"""...
"""
import polars as pl

conn = "sqlite:///media/alxfed/data/games/AC/sqlite/airport_payments.sqlite"
query1 = "SELECT * FROM payment_june_installs"

        # event_id, 
        # strftime('%m-%d-%Y %H:%M:%f', timestamp/1000.0, 'unixepoch')
# query2 = "SELECT * FROM payment_july"
# query3 = "SELECT * FROM payment_august_installs"
# query4 = "SELECT * FROM payment_september_installs"
# query5 = "SELECT * FROM payment_october_installs"

table = pl.read_sql(sql=[query1
    # , query2, query3, query4, query5
                         ], connection_uri=conn)
df = table.with_columns(
    [
        pl.col("timestamp").cast(pl.datatypes.Datetime),
        pl.col("price_usd").cast(pl.datatypes.Float64),
    ]
)
print('ok')
