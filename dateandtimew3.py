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
datestring = "Jan 25 2014 2:43PM"
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

#11. Write a Python program to convert Year/Month/Day to Day of Year in Python.  #RM:  print the day number of the year or day count of the year; e.g. Dec 31 is 365 day number.
monthdayyear = "04/10/2018"
datestringsplit = monthdayyear.split("/")
print(datestringsplit) #print ['04', '10', '2018']
dateformat = datestringsplit[0]+" "+datestringsplit[1]+" "+datestringsplit[2]
print(dateformat) #print 04 10 2018
print(datetime.strptime(dateformat, "%m %d %Y")) #print 2018-04-10 00:00:00
dateformat = datetime.strptime(dateformat, "%m %d %Y")
print(dateformat.strftime("%j")) #print 100
#quicker
monthdayyear = "04/10/2018"
print(datetime.strptime(monthdayyear, "%m/%d/%Y")) #print 2018-04-10 00:00:00
dateformat = datetime.strptime(monthdayyear, "%m/%d/%Y")
print(dateformat.strftime("%j")) #print 100

#12. Write a Python program to get current time in milliseconds in Python.
#copied solution
from time import time
milli_sec = int(round(time() * 1000))
print(milli_sec) #print 1553658720436

#13. Write a Python program to get week number. Go to the editor  Sample Date: 2015, 6, 16.  Expected Output: 25.
sampledate = "2015, 6, 16"
print(datetime.strptime(sampledate, "%Y, %m, %d")) #print 2015-06-16 00:00:00
weeknumberfromsampledate = datetime.strptime(sampledate, "%Y, %m, %d")
print(weeknumberfromsampledate.strftime("%W")) #print 24

#14. Write a Python program to find the date of the first Monday of a given week. Sample Year and week: 2015, 50.  Expected Output: Mon Dec 14 00:00:00 2015.  #source:  https://stackoverflow.com/questions/17087314/get-date-from-week-number.  https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior.
sampleyear = 2015
sampleweek = 50
sampleyearweek = "2015, 50"
firstmonday = datetime.strptime(sampleyearweek + "-1","%Y, %W-%w")
print(firstmonday) #print 2015-12-14 00:00:00
print(firstmonday.strftime("%a %b %d %Y")) #print Mon Dec 14 2015
firsttuesday = datetime.strptime(sampleyearweek + "-2","%Y, %W-%w")
print(firsttuesday) #print 2015-12-15 00:00:00
print(firsttuesday.strftime("%a %b %d %Y")) #print Tue Dec 15 2015
firstsaturday = datetime.strptime(sampleyearweek + "-6","%Y, %W-%w")
print(firstsaturday) #print 2015-12-19 00:00:00
print(firstsaturday.strftime("%a %b %d %Y")) #print Sat Dec 19 2015
#official solution
import time
print(time.asctime(time.strptime('2015 50 1', '%Y %W %w'))) #print Mon Dec 14 00:00:00 2015

#15. Write a Python program to select all the Sundays of a specified year.
year = str(2015)
for n in range(0,53):
	weekstring = str(n)
	yearweek = year+" "+weekstring
	sundays = datetime.strptime(yearweek + "-0","%Y %W-%w")
	print(sundays.strftime("%a %b %d %Y")) #print Sun Jan 04 2015 . . . Sun Jan 03 2016

#16. Write a Python program to add year(s) with a given date and display the new date.
"""
Sample Data: (addYears is the user defined function name) 
print(addYears(datetime.date(2015,1,1), -1))
print(addYears(datetime.date(2015,1,1), 0))
print(addYears(datetime.date(2015,1,1), 2))
print(addYears(datetime.date(2000,2,29),1))
Expected Output: 
2014-01-01
2015-01-01
2017-01-01
2001-03-01
"""
#Source:  https://stackoverflow.com/questions/32799428/adding-years-in-python.  #pip install python-dateutil
from dateutil.relativedelta import relativedelta
def addYears(year, month, day, yearchange):
	return date(year, month, day) + relativedelta(years=yearchange)
print(addYears(2015, 1, 1, -1)) #print 2014-01-01
print(addYears(2015, 1, 1, 0)) #print 2015-01-01
print(addYears(2015, 1, 1, 2)) #print 2017-01-01
print(addYears(2000, 2, 29, 1)) #print 2001-02-28

#17. Write a Python program to drop microseconds from datetime.
dtt = datetime.today()
print(dtt) #print 2019-04-02 14:23:43.737867
print(dtt.strftime("%m/%d/%y")) #print 04/02/19
now = datetime.now()
print(now) #print 2019-04-02 14:23:43.737961
print(now.strftime("%m/%d/%y")) #print 04/02/19

#18. Write a Python program to get days between two dates. Sample Dates: 2000,2,28, 2001,2,28.  Expected Output: 366 days, 0:00:00.  Source:  https://stackoverflow.com/questions/151199/how-to-calculate-number-of-days-between-two-given-dates
date1 = date(2000, 2, 28)
date2 = date(2001, 2, 28)
daysbetween = date2 - date1
print(daysbetween.days) #print 366

#19. Write a Python program to get the date of the last Tuesday.
#official solution
today = date.today()
offset = (today.weekday() - 1) % 7
print(offset) #print 0
last_tuesday = today - timedelta(days=offset)
print(last_tuesday) #print 2019-04-02
#RM:  the number to the right of (today.weekday() - dictates date of the last *blank*.  Today is Tue Apr 2.  If -0, then Mon Apr 1.  If -1, then Tue Apr 2.  If -2, then Wed Mar 27.  If -3, then Thur Mar 28.  If +1, then Sun Mar 31.  If +2, then Sat Mar 30.  If +3, the Fri Mar 29.  
dtt = datetime.today()
todaydate = dtt.strftime("%a")
lastdate = "Thu"
while True:
	if dtt.strftime("%a") == todaydate and dtt.strftime("%a") == lastdate:
		print("Actually "+lastdate+" is today " +dtt.strftime("%a %b %d, %Y.")+" However . . . ")
		todaydate = ""
		dtt = dtt - timedelta(days=1)
	elif dtt.strftime("%a") == lastdate:
		print("The last "+lastdate+" is " +dtt.strftime("%a %b %d, %Y"))
		break
	else:
		dtt = dtt - timedelta(days=1)