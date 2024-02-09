from pathlib import Path
import os
import glob
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
from collections import defaultdict

# find newest file in time management folder
# that corresponds to month that we are currently in

def rowing(iterable):
    iterator = iter(iterable)
    prev_item = None
    current_item = next(iterator)  # throws StopIteration if empty.
    for next_item in iterator:
        yield prev_item, current_item, next_item
        prev_item = current_item
        current_item = next_item
    yield prev_item, current_item, None


def exc(row):
    if not row.MONDAY.empty:
        Monday = row.MONDAY
    if not row.TUESDAY.empty:
        Tuesday = row.TUESDAY
    if not row.WEDNESDAY.empty:
        Wednesday = row.WEDNESDAY
    if not row.THURSDAY.empty:
        Thursday = row.THURSDAY
    if not row.FRIDAY.empty:
        Friday = row.FRIDAY
    if not row.SATURDAY.empty:
        Saturday = row.SATURDAY
    if not row.SUNDAY.empty:
        Sunday = row.SUNDAY
    return [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]


def doubble(Day):
    de = Day
    c = Day.shape[0] - 1

    count = 0
    while count <= c:
        de = Day.iloc[count, :]
        dp = de.shift()
        count += 1

        yield de, dp


def doubblec(de, dp, mid_format, first_monday_converted, count):

    counter = count + 1
    count_na = int
    size_of_de = de.size

    n_dict = defaultdict()
    l_list = []
    counting = count
    ncount = 0
    for description_de, time_de, description_dp, time_dp in zip(de, de.index, dp, dp.index):

        if description_de == description_dp:
            count_na += 1
            del l_list[-1]

        else:
            count_na = 1
            start_format = datetime.strptime(time_de, "%H:%M")

        start, end = timex(start_format, mid_format, first_monday_converted, counter, count, count_na)

        l_list.append([description_de, start, end, count_na])

    return l_list


def timex(start_format, mid_format, first_monday_converted, counter, count, count_na):

    if start_format <= mid_format:
        duration = mid_format - start_format

    else:
        duration = mid_format - start_format + timedelta(hours=24)

    timedelta_seven = timedelta(hours=19)
    timedelta_mid = timedelta(hours=0, minutes=0, seconds=0, microseconds=0)
    while True:
        if timedelta_mid < duration <= timedelta_seven:

            start_ed = start_format.replace(year=first_monday_converted.year,
                                            month=first_monday_converted.month,
                                            day=first_monday_converted.day + count)
            start = start_ed.isoformat()
            end = ((start_ed + count_na * timedelta(hours=0.5)).isoformat())

            return start, end
        else:
            start_ed = start_format.replace(year=first_monday_converted.year,
                                            month=first_monday_converted.month,
                                            day=first_monday_converted.day + counter)

            start = start_ed.isoformat()
            end = ((start_ed + count_na * timedelta(hours=0.5)).isoformat())

            return start, end



