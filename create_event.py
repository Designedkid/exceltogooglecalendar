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
    print(str_last_day)
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    mid = midnight.strftime("%H:%M")
   # creates one hour event tomorrow 10 AM IST
    if month_now in latest_file:
        csvcal = latest_file
        read_csv = pd.read_csv(csvcal, sep=';', header=0)
        time = read_csv[read_csv.columns[0]]
        read_csv.set_index('Time', inplace=True)

        for row in read_csv.itertuples():
            #print(row)
            description, start, end = etgc.exc(row, mid, first_monday_converted)
            service = get_calendar_service()
            #if description not 'nan':
            #print(description, start, end)
          #      event_result = service.events().insert(calendarId='timetable', body={

           #            "summary": event,
            #           "description": 'Timetable',
             #          "start": {"dateTime": start, "timeZone": 'Europe/Berlin'},
              #         "end": {"dateTime": end, "timeZone": 'Europe/Berlin'},
               #        'recurrence': [f'RRULE:FREQ=WEEKLY;UNTIL={str_last_day}']
               # }
               # ).execute()

         #   print("created event")
          #  print("id: ", event_result['id'])
           # print("summary: ", event_result['summary'])
           # print("starts at: ", event_result['start']['dateTime'])
           # print("ends at: ", event_result['end']['dateTime'])

if __name__ == '__main__':
   main()