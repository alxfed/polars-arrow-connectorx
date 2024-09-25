# -*- coding: utf-8 -*-
# Python
"""

"""
import pyarrow as pa

completion_schema = pa.schema([
        ('some_int', pa.int32()),
        ('some_string', pa.string())
    ])

b = pa.schema([
    pa.field('n_legs', pa.int64()),
    pa.field('animals', pa.string())],
    metadata={'n_legs': 'Number of legs per animal'})

m = b.metadata.decode("utf-8")

print('ok')