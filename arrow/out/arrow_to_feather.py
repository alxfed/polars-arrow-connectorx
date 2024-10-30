# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
import pyarrow as pa
from pyarrow import feather


days = pa.array([1, 12, 17, 23, 28], type=pa.int8())
months = pa.array([1, 3, 5, 7, 1], type=pa.int8())
years = pa.array([1990, 2000, 1995, 2000, 1995], type=pa.int16())

birthdays_table = pa.table([days, months, years], names=["days", "months", "years"])

feather.write_feather(birthdays_table, "../arrays/birthdays.feather")

arrow_table = feather.read_table('../arrays/birthdays.feather')

...