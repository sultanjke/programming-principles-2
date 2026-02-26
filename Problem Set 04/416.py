from datetime import datetime, timedelta, timezone

def parse_datetime(line):
    parts = line.split()
    date_str = parts[0]
    time_str = parts[1]
    tz_str = parts[2]

    year, month, day = map(int, date_str.split('-'))
    hour, minute, second = map(int, time_str.split(':'))

    sign = 1 if '+' in tz_str else -1
    tz_parts = tz_str.replace('UTC', '').replace('+', '').replace('-', '').split(':')
    hours = int(tz_parts[0])
    minutes = int(tz_parts[1])
    offset = timedelta(hours=sign * hours, minutes=sign * minutes)

    tz = timezone(offset)
    dt = datetime(year, month, day, hour, minute, second, tzinfo=tz)
    return dt

start = parse_datetime(input())
end = parse_datetime(input())

diff = int((end - start).total_seconds())
print(diff)
