from datetime import datetime, timedelta, timezone
import calendar

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
    return dt, month, day, tz

birth_line = input()
current_line = input()

birth_dt, birth_month, birth_day, birth_tz = parse_date(birth_line)
current_dt, _, _, _ = parse_date(current_line)

best = None
for y in range(current_dt.year - 1, current_dt.year + 3):
    bm = birth_month
    bd = birth_day
    if bm == 2 and bd == 29:
        if not calendar.isleap(y):
            bd = 28
    try:
        bday = datetime(y, bm, bd, 0, 0, 0, tzinfo=birth_tz)
    except ValueError:
        continue

    diff = (bday - current_dt).total_seconds()
    if diff >= 0:
        days = int(diff // 86400)
        if best is None or days < best:
            best = days

print(best)
