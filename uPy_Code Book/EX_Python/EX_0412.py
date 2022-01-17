"""
EX_0412 (Python DateTime)
Basic Python programming by appsofttech.com
"""
# Date

import datetime

print('get date/time')
print('Date/Time: ', end='')
dt = datetime.datetime.now()
print(dt)
print("Current day   :", dt.day)
print("Current month :", dt.month)
print("Current year  :", dt.year)

print('...')
