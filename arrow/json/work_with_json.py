# -*- coding: utf-8 -*-
# Python
from pyarrow import json

fn = 'my_data.jl'
table = json.read_json(fn)

print(table)