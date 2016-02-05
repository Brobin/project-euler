'''
How many Sundays fell on the first of the month during 
the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

import datetime


def first_day_sunday():
    count = 0
    for month in range(1, 13):
        for year in range(1901, 2001):
            first = datetime.datetime(year, month, 1)
            if first.weekday() == 6:
                count += 1
    return count

print(first_day_sunday())
