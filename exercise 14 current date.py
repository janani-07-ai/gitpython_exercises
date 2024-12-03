# write a program to find current date
from typing import dataclass_transform

import datetime as dt
current_date=dt.date.today()
print(current_date)
print(current_date.year)
print(current_date.month)
print(current_date.day)
current_time=dt.datetime.now()
print(current_time)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)




