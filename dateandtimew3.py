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

#4. Write a Python program to get the current time in Python.  Sample Format:  13:19:49.078205.
dtt = datetime.today()
print(dtt) #print 2019-03-22 19:08:38.607919
print(dtt.hour) #print 19
print(dtt.minute) #print 8
print(dtt.second) #print 38
print("Time is %s:%s:%s" % (dtt.hour, dtt.minute, dtt.second)) #print Time is 19:8:38
print("Time is {}:{}:{}".format(dtt.hour, dtt.minute, dtt.second)) #print Time is 19:8:38
dttt = datetime.today().time()
print(dttt) #print 19:08:38.608087

#5. Write a Python program to subtract five days from current date.
dtt = datetime.today()
print("Today is",dtt.strftime("%m/%d/%y")) #print Today is 03/22/19
fivedaysago = str(int(dtt.strftime("%d"))-5)
print("Five days ago is",dtt.strftime("%m")+"/"+fivedaysago+"/"+dtt.strftime("%y")) #print Five days ago is 03/17/19
#official solution
from datetime import timedelta
dtttimedelta = datetime.today() - timedelta(5)
print("Five days ago is",dtttimedelta) #print Five days ago is Five days ago is 2019-03-17 19:19:22.872699
from datetime import date, timedelta
dt = date.today() - timedelta(5)
print('Current Date :',date.today()) #print Current Date: 2019-03-22
print('5 days before Current Date :',dt) #print 5 days before Current Date: 2019-03-17

#6. Write a Python program to convert unix timestamp string to readable date. Sample Unix timestamp string: 1284105682.  Expected Output: 2010-09-10 13:31:22.
#official solution
print(datetime.fromtimestamp(int("1284105682")).strftime('%Y-%m-%d %H:%M:%S')) #print 2010-09-10 01:01:22

#7. Write a Python program to print yesterday, today, tomorrow.
from datetime import date
dt = date.today()
print(dt) #print 2019-03-22
print(dt.strftime("%m/%d/%y")) #print 03/22/19
dtyesterday = str(int(dt.strftime("%d"))-1)
dttomorrow = str(int(dt.strftime("%d"))+1)
print("Yesterday was "+dt.strftime("%m")+"/"+dtyesterday+"/"+dt.strftime("%y")) #print Yesterday was 03/21/19
print("Tomorrow is "+dt.strftime("%m")+"/"+dttomorrow+"/"+dt.strftime("%y")) #print Tomorrow is 03/23/19
from datetime import timedelta
dtyesterday2 = dt.today() - timedelta(1)
dttomorrow2 = dt.today() + timedelta(1)
print("Yesterday was",dtyesterday2) #print Yesterday was 2019-03-21
print("Tomorrow is",dttomorrow2) #print Tomorrow is 2019-03-23

#8. Write a Python program to convert the date to datetime (midnight of the date) in Python.  Sample Output: 2015-06-22 00:00:00
assigndate = "06/22/2015"
print(datetime.strptime(assigndate, "%m/%d/%Y")) #print 2015-06-22 00:00:00

#9. Write a Python program to print next 5 days starting from today.
dt = date.today()
for n in range(0,5):
	nextday = dt + timedelta(n)
	print(nextday)
'''
2019-03-22
2019-03-23
2019-03-24
2019-03-25
2019-03-26
'''

#10. Write a Python program to add 5 seconds with the current time.
#additional information https://stackoverflow.com/questions/656297/python-time-timedelta-equivalent
from datetime import date, datetime, time, timedelta
dttt = datetime.today().time()
print(dttt) #print 20:00:49.896064
print(type(dttt)) #print <class 'datetime.time'>.  RM:  it's not <class 'datetime.datetime'>
#fiveseconds = dttt + timedelta(minutes=5)
fiveseconds = datetime.combine(date.today(), time(dttt.hour, dttt.minute, dttt.second)) + timedelta(seconds=5)
print(fiveseconds.time()) #print 20:00:54