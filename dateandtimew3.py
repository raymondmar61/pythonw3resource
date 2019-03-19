#https://www.w3resource.com/python-exercises/date-time-exercise/
from datetime import datetime
#1. Write a Python script to display the various Date Time formats
'''
a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week
'''
now = datetime.now()
print("a1) Current date and time--> datetime.now(): {}".format(datetime.now()))
print("a2) Current date and time--> now: {}".format(now))
print("b) Current year-->now.year: {}".format(now.year))
print("c) Month of year-->now.month: {}".format(now.month))

