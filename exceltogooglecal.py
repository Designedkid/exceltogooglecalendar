from pathlib import Path
import os
import glob
import pandas as pd
from datetime import datetime, timedelta
import numpy as np


# find newest file in time management folder
# that corresponds to month that we are currently in


def desc(row):
    for r in row:
        print(r)
    #description

def exc(row, mid, first_monday_converted):

    if row.MONDAY:
        description = row.MONDAY
        start_row = row[0]

        start_format = datetime.strptime(start_row, "%H:%M")
        mid_format = datetime.strptime(mid, "%H:%M")

        if start_format <= mid_format:
            duration = mid_format - start_format

        else:
            duration = mid_format - start_format + timedelta(hours=24)

        timedelta_seven = timedelta(hours=19)
        timedelta_mid = timedelta(hours=0, minutes=0, seconds=0, microseconds=0)
        while True:
            if timedelta_mid < duration <= timedelta_seven:

                start_ed = start_format.replace(year=first_monday_converted.year, month=first_monday_converted.month,
                                                                         day=first_monday_converted.day)
                start = start_ed.isoformat()
                end = ((start_ed + timedelta(hours=0.5)).isoformat())

                break
            else:
                start_ed = start_format.replace(year=first_monday_converted.year,
                                                month=first_monday_converted.month,
                                                day=first_monday_converted.day + 1)

                start = start_ed.isoformat()
                end = ((start_ed + timedelta(hours=0.5)).isoformat())

                break
        return description, start, end
    if row.TUESDAY:
        description = row.TUESDAY

        start_row = row[0]
        print(start_row)
        start_format = datetime.strptime(start_row, "%H:%M")
        mid_format = datetime.strptime(mid, "%H:%M")

        if start_format <= mid_format:
            duration = mid_format - start_format

        else:
            duration = mid_format - start_format + timedelta(hours=24)

        timedelta_seven = timedelta(hours=19)
        timedelta_mid = timedelta(hours=0, minutes=0, seconds=0, microseconds=0)
        while True:
            if timedelta_mid < duration <= timedelta_seven:

                start_ed = start_format.replace(year=first_monday_converted.year, month=first_monday_converted.month,
                                                                         day=first_monday_converted.day+1)
                start = start_ed.isoformat()
                end = ((start_ed + timedelta(hours=0.5)).isoformat())

                break
            else:
                start_ed = start_format.replace(year=first_monday_converted.year,
                                                month=first_monday_converted.month,
                                                day=first_monday_converted.day + 2)

                start = start_ed.isoformat()
                end = ((start_ed + timedelta(hours=0.5)).isoformat())

                break
        return description, start, end
    elif row.WEDNESDAY:
        description = row.WEDNESDAY
        start_row = row[0]
        start_format = datetime.strptime(start_row, "%H:%M")
        mid_format = datetime.strptime(mid, "%H:%M")

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
                                                day=first_monday_converted.day + 2)
                start = start_ed.isoformat()
                end = ((start_ed + timedelta(hours=0.5)).isoformat())

                break
            else:
                start_ed = start_format.replace(year=first_monday_converted.year,
                                                month=first_monday_converted.month,
                                                day=first_monday_converted.day + 3)

                start = start_ed.isoformat()
                end = ((start_ed + timedelta(hours=0.5)).isoformat())

                break
        return description, start, end
    elif row.THURSDAY:
        description = row.THURSDAY
        start_row = row[0]
        start_format = datetime.strptime(start_row, "%H:%M")
        mid_format = datetime.strptime(mid, "%H:%M")

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
                                                day=first_monday_converted.day + 3)
                start = start_ed.isoformat()
                end = ((start_ed + timedelta(hours=0.5)).isoformat())

                break
            else:
                start_ed = start_format.replace(year=first_monday_converted.year,
                                                month=first_monday_converted.month,
                                                day=first_monday_converted.day + 4)

                start = start_ed.isoformat()
                end = ((start_ed + timedelta(hours=0.5)).isoformat())

                break
    elif row.FRIDAY:
        description = row.FRIDAY
        start_row = row[0]
        start_format = datetime.strptime(start_row, "%H:%M")
        mid_format = datetime.strptime(mid, "%H:%M")

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
                                                day=first_monday_converted.day + 4)
                start = start_ed.isoformat()
                end = ((start_ed + timedelta(hours=0.5)).isoformat())

                break
            else:
                start_ed = start_format.replace(year=first_monday_converted.year,
                                                month=first_monday_converted.month,
                                                day=first_monday_converted.day + 5)

                start = start_ed.isoformat()
                end = ((start_ed + timedelta(hours=0.5)).isoformat())

                break
    elif row.SATURDAY:
        description = row.SATURDAY
        start_row = row[0]
        start_format = datetime.strptime(start_row, "%H:%M")
        mid_format = datetime.strptime(mid, "%H:%M")

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
                                                day=first_monday_converted.day + 5)
                start = start_ed.isoformat()
                end = ((start_ed + timedelta(hours=0.5)).isoformat())

                break
            else:
                start_ed = start_format.replace(year=first_monday_converted.year,
                                                month=first_monday_converted.month,
                                                day=first_monday_converted.day + 6)

                start = start_ed.isoformat()
                end = ((start_ed + timedelta(hours=0.5)).isoformat())

                break
    elif row.SUNDAY:
        description = row.SUNDAY
        start_row = row[0]
        start_format = datetime.strptime(start_row, "%H:%M")
        mid_format = datetime.strptime(mid, "%H:%M")

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
                                                day=first_monday_converted.day + 6)
                start = start_ed.isoformat()
                end = ((start_ed + timedelta(hours=0.5)).isoformat())

                break
            else:
                start_ed = start_format.replace(year=first_monday_converted.year,
                                                month=first_monday_converted.month,
                                                day=first_monday_converted.day + 7)

                start = start_ed.isoformat()
                end = ((start_ed + timedelta(hours=0.5)).isoformat())

                break





