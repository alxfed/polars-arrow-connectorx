# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
import pyarrow as pa
import numpy as np

arr = pa.array(np.arange(100))

schema = pa.schema([
    pa.field('numbers', arr.type)
])

with pa.OSFile('../arrays/arraydata2.arrow', 'wb') as sink:
    with pa.ipc.new_file(sink, schema=schema) as writer:
        batch = pa.record_batch([arr], schema=schema)
        writer.write(batch)

print('ok')