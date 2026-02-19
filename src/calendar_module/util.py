import calendar

def get_day(m,d,y):
    fdate = calendar.weekday(y, m, d)
    print(calendar.day_name[fdate].upper())