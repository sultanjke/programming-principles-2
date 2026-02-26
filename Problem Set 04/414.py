from datetime import datetime, timedelta, timezone

def parse_date(line):
    parts = line.split()
    date_str = parts[0]
    tz_str = parts[1]

    year, month, day = map(int, date_str.split('-'))

    sign = 1 if '+' in tz_str else -1
    tz_parts = tz_str.replace('UTC', '').replace('+', '').replace('-', '').split(':')
    hours = int(tz_parts[0])
    minutes = int(tz_parts[1])
    offset = timedelta(hours=sign * hours, minutes=sign * minutes)

    tz = timezone(offset)
    dt = datetime(year, month, day, 0, 0, 0, tzinfo=tz)
    return dt

line1 = input()
line2 = input()

dt1 = parse_date(line1)
dt2 = parse_date(line2)

diff = abs((dt2 - dt1).total_seconds())
print(int(diff // 86400))
