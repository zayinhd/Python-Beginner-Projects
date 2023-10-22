# Example : 
# input your name: Abc
# input your age: 20 
# Output : XYZ's age is 20 years or 250 months or 7578 days

import time
from calendar import isleap

#check if a year is a leap year
def is_leap_year(year):
    if isleap(year):
        return True
    else:
        return False

#return number of days of a month
def days_of_month(month, leap_year):
    if month in [4,6,9,11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28
    else:
        return 31
    

localtime = time.localtime()

name = input("Please, Enter your name : ")
age = input("Please, Enter your age : ")

year = int(age) #10
month = year * 12 + localtime.tm_mon
day = 0

#get year of birth and the current year
start_year = int(localtime.tm_year) - year
end_year = int(localtime.tm_year)

#calculate the days
for y in range(start_year, end_year):
    if(is_leap_year(y)):
        day = day + 366
    else:
        day = day + 365

#add the current year days to day
leap_year = is_leap_year(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    day = day + days_of_month(m, leap_year)
        
print("%s's age is %d years or "%(name, year), end="")
print("%d months or %d days"%(month, day))
