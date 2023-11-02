
import datetime

t_day = datetime.date.today()
print(t_day)

# this count monday as 0 and sunday as 6
print(t_day.weekday())

# counts monday as 1 and sunday as 7
print(t_day.isoweekday())

t_delta = datetime.timedelta(days=18)
print(t_day + t_delta)

b_day = datetime.date(2022, 7, 3)
v_day = datetime.date(2022, 2, 14)
time_delta = b_day - t_day
time_del = v_day - t_day
print(time_delta.days)
print(time_del.days)
