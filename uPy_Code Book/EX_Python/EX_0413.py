"""
EX_0413 (Python DateTime)
Basic Python programming by appsofttech.com
"""
# Time

import datetime

print('get time')
print('Date/Time: ', end='')
tm = datetime.datetime.now()
print(tm)
print("hour        :", tm.hour)
print("minute      :", tm.minute)
print("second      :", tm.second)
print("microsecond :", tm.microsecond)

print('...')
