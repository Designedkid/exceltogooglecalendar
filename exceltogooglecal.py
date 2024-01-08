from pathlib import Path
import os
import glob
import pandas as pd
from datetime import datetime, timedelta
import numpy as np


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
    if row.MONDAY:
        description_mon = row.MONDAY
    if row.TUESDAY:
        description_tue = row.TUESDAY
    if row.WEDNESDAY:
        description_wed = row.WEDNESDAY
    if row.THURSDAY:
        description_thu = row.THURSDAY
    if row.FRIDAY:
        description_fri = row.FRIDAY
    if row.SATURDAY:
        description_sat = row.SATURDAY
    if row.SUNDAY:
        description_sun = row.SUNDAY
    return [description_mon, description_tue, description_wed,description_thu, description_fri, description_sat, description_sun]


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



