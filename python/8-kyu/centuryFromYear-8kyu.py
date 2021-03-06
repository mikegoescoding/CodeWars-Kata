# Century From Year
# 8kyu

'''
The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to and including the year 200, etc.

Task :
Given a year, return the century it is in.

Input , Output Examples ::
centuryFromYear(1705)  returns (18)
centuryFromYear(1900)  returns (19)
centuryFromYear(1601)  returns (17)
centuryFromYear(2000)  returns (20)
Hope you enjoy it .. Awaiting for Best Practice Codes

Enjoy Learning !!!
'''

import math

def century(year):
    if year % 100 == 0:
        return (year // 100)
    divided_year = year / 100
    rounded_year = math.ceil(divided_year)
    return rounded_year

print(century(1776))
print(century(1505))
print(century(1905))