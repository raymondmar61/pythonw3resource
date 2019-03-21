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
print(type(now)) #print <class 'datetime.datetime'>
print("now = datetime.now()") #print now = datetime.now()
print("a) Current date and time--> datetime.now(): {}".format(datetime.now())) #print a) Current date and time--> datetime.now(): 2019-03-20 21:05:01.162086
print("a) Current date and time--> now: {}".format(now)) #print a) Current date and time--> now: 2019-03-20 21:05:01.162044
print("b) Current year-->now.year: {}".format(now.year)) #print b) Current year-->now.year: 2019
print("c) Month of year-->now.month: {}".format(now.month)) #print c) Month of year-->now.month: 3
print("g) Day of the month-->now.day: {}".format(now.day)) #print g) Day of the month-->now.day: 20
print("\n")

dtt = datetime.today()
print(type(dtt)) #print <class 'datetime.datetime'> 
print("dtt = datetime.today()") #print dtt = datetime.today()
print("a) Current date and time-->dtt.now(): {}".format(dtt.now())) #print a) Current date and time-->dtt.now(): 2019-03-20 21:05:01.162183
print("b) Current Year-->dtt.strftime(\"%Y\"): {}".format(dtt.strftime("%Y"))) #print b) Current Year-->dtt.strftime("%Y"): 2019
print("b) Current Year-->dtt.strftime(\"%y\"): {}".format(dtt.strftime("%y"))) #print b) Current Year-->dtt.strftime("%y"): 19
print("c) Month of year-->dtt.strftime(\"%B\"): {}".format(dtt.strftime("%B"))) #print c) Month of year-->dtt.strftime("%B"): March
print("c) Month of year-->dtt.strftime(\"%b\"): {}".format(dtt.strftime("%b"))) #print c) Month of year-->dtt.strftime("%b"): Mar
print("c) Month of year-->dtt.strftime(\"%m\"): {}".format(dtt.strftime("%m"))) #print c) Month of year-->dtt.strftime("%m"): 03
print("d) Week number of the year-->dtt.strftime(\"%W\"): {}".format(dtt.strftime("%W"))) #print d) Week number of the year-->dtt.strftime("%W"): 11
print("e) Weekday of the week-->dtt.strftime(\"%w\"): {}".format(dtt.strftime("%w"))) #print e) Weekday of the week-->dtt.strftime("%w"): 3
print("f) Day of year-->dtt.strftime(\"%j\"): {}".format(dtt.strftime("%j"))) #print f) Day of year-->dtt.strftime("%j"): 079
print("g) Day of month-->dtt.strftime(\"%d\"): {}".format(dtt.strftime("%d"))) #print g) Day of month-->dtt.strftime("%d"): 20
print("h) Day of week-->dtt.strftime(\"%A\"): {}".format(dtt.strftime("%A"))) #print h) Day of week-->dtt.strftime("%A"): Wednesday
print("h) Day of week-->dtt.strftime(\"%a\"): {}".format(dtt.strftime("%a"))) #print h) Day of week-->dtt.strftime("%a"): Wed
print("Today is",dtt.strftime("%a %b %y")) #print Today is Wed Mar 19
print("Today is "+dtt.strftime("%a %b %y")) #print Today is Wed Mar 19
print("Today is",dtt.strftime("%m/%d/%y")) #print Today is 03/20/19

#2. Write a Python program to determine whether a given year is a leap year.
import calendar
print(calendar.isleap(1900)) #print False
#also
def isleapyear(year):
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(isleapyear(1900)) #print False

#3. Write a Python program to convert a string to datetime. Sample String: Jan 25 2014 2:43PM.  Expected Output: 2014-07-25 14:43:00  #RM:  override to Jan 25.
datestring = "Jan 25 2014 2:43PM"
datestringsplit = datestring.split()
print(datestringsplit) #print ['Jan', '25', '2014', '2:43PM']
dateformat = datestringsplit[0]+"/"+datestringsplit[1]+"/"+datestringsplit[2]+" "+datestringsplit[3]
print(dateformat) #print Jan/25/2014 2:43PM
print(datetime.strptime(dateformat, "%b/%d/%Y %I:%M%p")) #print 2014-01-25 14:43:00
#quicker
datestring = "Jan 25 2014 2:43PM"
print(datetime.strptime(datestring, "%b %d %Y %I:%M%p")) #print 2014-01-25 14:43:00
#bonus
print(type(datetime.strptime(datestring, "%b %d %Y %I:%M%p"))) #print <class 'datetime.datetime'>
print(datetime.strptime(datestring, "%b %d %Y %I:%M%p").strftime('%b %d, %Y %I:%M:%S %p')) #print Jan 25, 2014 02:43:00 PM
print(datetime.strptime(datestring, "%b %d %Y %I:%M%p").strftime('%B %d, %Y %I:%M:%S %p')) #print January 25, 2014 02:43:00 PM
print(datetime.strptime(datestring, "%b %d %Y %I:%M%p").strftime('%B %d, %Y %I:%M %p')) #print January 25, 2014 02:43 PM
print(datetime.strptime(datestring, "%b %d %Y %I:%M%p").strftime('%B %d, %Y %-I:%M %p')) #print January 25, 2014 2:43 PM #tip https://coderwall.com/p/drqn9g/removing-leading-zeroes-in-python-s-strftime