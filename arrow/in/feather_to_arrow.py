# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from pyarrow import feather


arrow_table = feather.read_table('../arrays/birthdays.feather')
...