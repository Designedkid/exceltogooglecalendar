from datetime import datetime, timedelta
from cal_setup import get_calendar_service
import exceltogooglecal as etgc
from pathlib import Path
import os
import glob
from datetime import datetime, timedelta
import numpy as np
import re
import pandas as pd
from collections import defaultdict


def main():
    target_dir = 'C:\\Users\\abdur\\Documents\\Time Management\\*.csv'
    list_of_files = glob.glob(target_dir)
    latest_file = max(list_of_files, key=os.path.getctime)

    now = datetime.now()
    month_now = now.strftime('%B')
    monday = now - timedelta(days=now.weekday())
    # first monday in the month
    any_date_in_month = datetime.date(now)

    year_month = any_date_in_month.strftime('%Y-%m')
    first_monday = np.busday_offset(year_month, 0, roll='forward', weekmask='Mon')
    dt64 = np.datetime64(first_monday)
    unix_epoch = np.datetime64(0, "s")
    one_second = np.timedelta64(1, "s")
    seconds_since_epoch = (dt64 - unix_epoch) / one_second
    first_monday_converted = datetime.utcfromtimestamp(seconds_since_epoch)

    #last day of the month
    next_month = first_monday_converted.replace(day=28) + timedelta(days=4)
    last_day_month = next_month - timedelta(days=next_month.day)
    str_last_day = re.sub(":|-", "", str(last_day_month.isoformat()))
    str_last_day = str_last_day + "Z"
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    mid = midnight.strftime("%H:%M")
    service = get_calendar_service()
    mid_format = datetime.strptime(mid, "%H:%M")

    if month_now in latest_file:
        csvcal = latest_file
        read_csv = pd.read_csv(csvcal, sep=';', header=0)
        read_csv = read_csv.ffill()
        time = read_csv[read_csv.columns[0]]
        Day = etgc.exc(read_csv)
        #print(Day)
        df_day = pd.DataFrame(Day)
        #df_time_day = pd.DataFrame(df_day.values, columns=time)
        df_day = df_day.set_axis(time, axis=1)
        #print(df_day)
        counting = 0
        for de, dp in etgc.doubble(df_day):

            n_dict = etgc.doubblec(de, dp, mid_format, first_monday_converted, counting)
            counting += 1

            for d_item in n_dict:
                description = d_item[0]
                start = d_item[1]
                end = d_item[2]

                event_result = service.events().insert(
                    calendarId='97e10ab365026c21e1454e9a38b84b45eae037fed4e466c9e73fdad50ff0fce4@group.calendar.google.com',
                    body={

                        "summary": description,
                        "description": 'Timetable',
                        "start": {"dateTime": start, "timeZone": 'Europe/Berlin'},
                        "end": {"dateTime": end, "timeZone": 'Europe/Berlin'},
                        'recurrence': [f'RRULE:FREQ=WEEKLY;UNTIL={str_last_day}']
                    }
                 ).execute()

                print("created event")
                print("id: ", event_result['id'])
                print("summary: ", event_result['summary'])
                print("starts at: ", event_result['start']['dateTime'])
                print("ends at: ", event_result['end']['dateTime'])


if __name__ == '__main__':
    main()
