# Calendar Module

import calendar

m, d, y=map(int,input().strip().split())

day_of_week = calendar.weekday(y, m, d)

if day_of_week == 0:
    print("MONDAY")
elif day_of_week == 1:
    print("TUESDAY")
elif day_of_week == 2:
    print("WEDNESDAY")
elif day_of_week == 3:
    print("THURSDAY")
elif day_of_week == 4:
    print("FRIDAY")
elif day_of_week == 5:
    print("SATURDAY")
elif day_of_week == 6:
    print("SUNDAY")
else:
    pass
