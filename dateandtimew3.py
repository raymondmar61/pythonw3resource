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
print("Today is",dtt.strftime("%a %b %d")) #print Today is Wed Mar 20
print("Today is "+dtt.strftime("%a %b %d")) #print Today is Wed Mar 20
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
lastdate = "Thu"  #RM:  choose Thursday Thu to remind myself Thursday is Thu three letter abbreviation.
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

#20. Write a Python program to test the third Tuesday of a month.
print(date(2019,3,25)) #print 2019-03-25
firstdayofmonth = date(2019,3,1)
counter = 0
while True:
	if firstdayofmonth.strftime("%a") == "Tue":
		counter += 1
	if counter == 3:
		print("The third Tuesday of the month is",firstdayofmonth.strftime("%a %b %d")) #print The third Tuesday of the month is Tue Mar 19
		break
	firstdayofmonth = firstdayofmonth+timedelta(days=1)

#21. Write a Python program to get the last day of a specified year and month.
year = 2019
month = 4
for days in range(31,27,-1):
	try:
		print("The last day of the month is",date(year,month,days).strftime("%a %b %d, %Y")) #print The last day of the month is Tue Apr 30, 2019
		break
	except ValueError:
		continue
	else:
		print("Doesn't work yet")
year = 2008
for month in range(1,13):
	for days in range(31,27,-1):
		try:
			print("The last day of the month is",date(year,month,days).strftime("%a %b %d, %Y")) #print The last day of the month is Fri Feb 29, 2008
			break
		except ValueError:
			continue
		else:
			print("Doesn't work yet")
#https://stackoverflow.com/questions/42950/get-last-day-of-the-month-in-python
def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + timedelta(days=4)
    return next_month - timedelta(days=next_month.day)
for month in range(1, 13):
	print(last_day_of_month(date(2012, month, 1)))

#22. Write a Python program to get the number of days of a given month and year.
from calendar import monthrange
#monthrange(year, month).  Returns weekday of first day of the month and number of days in month, for the specified year and month.  0 is Mon, 4 is Fri and 6 is Sun.
print(monthrange(2019,3))  #print (4,31)
print(monthrange(2019,3)[1])  #print 31
print(monthrange(2019,4))  #print (0,30)
print(monthrange(2019,4)[1])  #print 30

#23. Write a Python program to add a month with a specified date.
#RM:  take a look at question 26 because it seems inaccurate.
now = date.today()
print(now) #print 2019-04-22
sixmonthslater = now + relativedelta(months=+6)
print(sixmonthslater) #print 2019-10-22
sixmonthsearlier = now + relativedelta(months=-6)
print(sixmonthsearlier) #print 2018-10-22

#24. Write a Python program to count the number of Monday of the 1st day of the month from 2015 to 2016.
count = 0
for month in range(1,13):
	for year in range(2015,2017):
		assigndate = date(year,month,1)
		if assigndate.strftime("%a") == "Mon":
			count += 1
print("There are",count,"Mondays.") #print There are 3 Mondays.

#25. Write a Python program to print a string five times, delay three seconds.
#import time sleep() function is used to delay or slowdown your program in seconds.  time.sleep(seconds).  for x in range(0,61):  print(x) time.sleep(1)
from time import sleep
string = "Print a string."
for printstringfivetimes in range(0,5):
	print(string)
	sleep(3) #print Print a string.\n Print a string.\n Print a string.\n Print a string.\n Print a string.

#26. Write a Python program calculates the date six months from the current date using the datetime module.  Add months.  Add a month.  Date change.
#RM:  copied solution.  Also, it's inaccurate.
#Source:  https://stackoverflow.com/questions/546321/how-do-i-calculate-the-date-six-months-from-the-current-date-using-the-datetime
print((date.today() + timedelta(6*365/12)).isoformat()) #print 2019-10-21

#27. Write a Python program to create 12 fixed dates from a specified date over a given period. The difference between two dates will be 20.  Date add dates.
dtn = datetime.now()
print(dtn) #print 2019-04-22 14:20:30.684982
dt = date.today()
print(dt) #print 2019-04-22
print(dt + relativedelta(days=+20))
dt = date.today() #print 2019-04-22
for numberfixeddates in range(0,13):
	print(dt + relativedelta(days=+20)) #print 2019-05-12\n 2019-06-01\n 2019-06-21\n 2019-07-11\n 2019-07-31\n . . . 2019-12-18\n 2020-01-07\n
	dt = (dt + relativedelta(days=+20))
#also
dt = date.today() #print 2019-04-22
for numberfixeddates in range(0,13):
	print(dt + timedelta(days=+20)) #print 2019-05-12\n 2019-06-01\n 2019-06-21\n 2019-07-11\n 2019-07-31\n . . . 2019-12-18\n 2020-01-07\n
	dt = (dt + timedelta(days=+20))

#28. Write a Python program to get the dates 30 days before and after from the current date.
dt = date.today()
print(dt) #print 2019-04-22
print("30 days earlier",dt+timedelta(days=-30)) #print 30 days earlier 2019-03-23
print("30 days later",dt+timedelta(days=+30)) #print 30 days later 2019-05-22

#29. Write a Python program to get the GMT and local current time.  GMT stands for Greenwich Mean Time.
from time import gmtime, strftime
dtn = datetime.now()
print(dtn) #print 2019-04-22 14:41:13.549272
print(gmtime()) #print time.struct_time(tm_year=2019, tm_mon=4, tm_mday=22, tm_hour=21, tm_min=41, tm_sec=13, tm_wday=0, tm_yday=112, tm_isdst=0)
print("GMT Time time.strftime: "+strftime("%I:%M:%S %p %Z", gmtime())) #print GMT Time time.strftime: 09:41:13 PM GMT
print("Local time strftime: "+strftime("%I:%M:%S %p")) #print Local time strftime: 02:41:13 PM
print("Local time dtn.strftime: "+dtn.strftime("%I:%M:%S %p")) #print Local time dtn.strftime: 02:41:13 PM

#30. Write a Python program to convert a date to the timestamp.
import time
dt = date.today()
print(dt)
print("Local time dt.strftime: "+dt.strftime("%I:%M:%S %p")) #print Local time dt.strftime: 12:00:00 AM
dtn = datetime.now()
print(dtn) #print 2019-04-22 14:49:58.616290
print("Local time dtn.strftime: "+dtn.strftime("%I:%M:%S %p")) #print Local time dt.strftime: 02:49:58 PM
#official solution
print(time.mktime(dt.timetuple())) #print 1555916400.0

#31. Write a Python program to convert a string date to the timestamp.
from time import mktime
datestring = "Jan 25 2014 2:43PM"
print(datetime.strptime(datestring, "%b %d %Y %I:%M%p")) #print 2014-01-25 14:43:00
datestring = datetime.strptime(datestring, "%b %d %Y %I:%M%p")
print("Local time datestring.strftime: "+datestring.strftime("%I:%M:%S %p")) #print Local time datestring.strftime: 02:43:00 PM
print(mktime(datestring.timetuple())) #print 1390689780.0

#32. Write a Python program to calculate a number of days between two dates.
#https://stackoverflow.com/questions/151199/how-to-calculate-number-of-days-between-two-given-dates
datetoday = date.today()
datepast = date(2015, 4, 30)
daysbetween = datetoday - datepast
print(daysbetween.days) #print 1455

#33. Write a Python program to calculate no of days between two datetimes.
dtn = datetime.now()
print(dtn) #print 2019-04-24 13:56:13.068859
datetimepast = datetime(2015,4,30,18,2,59)
print(datetimepast) #print 2015-04-30 18:02:59
print(type(datetimepast)) #print <class 'datetime.datetime'>
daysbetween = dtn - datetimepast
print(daysbetween.days) #print 1454

#34. Write a Python program to display the date and time in a human-friendly string.
dtn = datetime.now()
print(dtn) #print 2019-04-24 13:56:13.068859
print("Today is",dtn.strftime("%a %b %d")) #print Today is Wed Apr 24
print("Today is "+dtn.strftime("%A %B %d")) #print Today is Today is Wednesday April 24
print("Today is",dtn.strftime("%m/%d/%y")) #print Today is 04/24/19
print("Today is "+dtn.strftime("%a %b %d, %Y")) #print Today is Wed Apr 24, 2019 

#35. Write a Python program to convert a date to Unix timestamp.
#copied solution
dt = datetime(2016, 2, 25, 23, 23)
print("Unix Timestamp: ",(mktime(dt.timetuple())))  #print Unix Timestamp:  1456471380.0
dtn = datetime.now()
print("Unix Timestamp now: ",(mktime(dtn.timetuple())))  #print Unix Timestamp now:  1556139844.0

#36. Write a Python program to calculate two date difference in seconds.
#source: https://stackoverflow.com/questions/4362491/how-do-i-check-the-difference-in-seconds-between-two-dates
datetoday = date.today()
datepast = date(2015, 4, 30)
daysbetween = datetoday - datepast
print(daysbetween.seconds) #print 0
print(daysbetween.total_seconds()) #print 125712000.0
dtn = datetime.now()
print(dtn) #print 2019-04-24 14:11:04.636388
datetimepast = datetime(2015,4,30,18,2,59)
print(datetimepast) #print 2015-04-30 18:02:59
daysbetween = dtn - datetimepast
print(daysbetween.seconds,"is incorrect") #print 72485 is incorrect
print(daysbetween.total_seconds()) #print 125697977.614781

#37. Write a Python program to convert two date difference in days, hours, minutes, seconds.
#Source: https://stackoverflow.com/questions/25439279/python-calculating-time-difference-to-give-years-months-days-hours-minutes
from dateutil.relativedelta import relativedelta
today = datetime.now()
print(today) #print 2019-04-24 14:23:27.689348
past = datetime(2015,4,30,18,2,59)
print(past) #print 2015-04-30 18:02:59
difference = relativedelta(today,past)
print(difference) #print relativedelta(years=+3, months=+11, days=+24, hours=+20, minutes=+20, seconds=+28, microseconds=+689348)
print("The difference is %d year %d month %d days %d hours %d minutes %d seconds" % (difference.years, difference.months, difference.days, difference.hours, difference.minutes, difference.seconds)) #print The difference is 3 year 11 month 24 days 20 hours 20 minutes 28 seconds

#38. Write a Python program to get last modified information of a file.

#39. Write a Python program to calculate an age in year.
from dateutil.relativedelta import relativedelta
today = datetime.now()
print(today) #print 2019-04-24 14:30:15.393683
past = date(1997,12,21)
print(past) #print 1997-12-21
difference = relativedelta(today,past)
print(difference) #print relativedelta(years=+21, months=+4, days=+3, hours=+14, minutes=+30, seconds=+15, microseconds=+393683)
print("The difference is %d years" % (difference.years)) #print The difference is 21 years

#40. Write a Python program to get the current date time information.
dtn = datetime.now()
print(dtn) #print 2019-04-24 14:35:35.976582
dtt = datetime.today()
print(dtt) #print #print 2019-04-24 14:35:35.976632
dt = date.today()
print(dt) #print 2019-04-24

