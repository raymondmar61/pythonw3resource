#https://www.w3resource.com/python-exercises/dictionary/

#1. Write a Python script to sort (ascending and descending) a dictionary by value.
stocks = {"GOOG": 520.54, "FB": 76.45, "YHOO": 39.28, "AMZN": 305.21, "AAPL": 99.76}
print(sorted(zip(stocks.values(), stocks.keys()))) #print [(39.28, 'YHOO'), (76.45, 'FB'), (99.76, 'AAPL'), (305.21, 'AMZN'), (520.54, 'GOOG')] values sorted smallest to largest
for price in sorted(stocks.values()): #sorted() function returns keys in order
	print(price) #print 39.28\n 76.45\n 99.76\n 305.21\n 520.54
from operator import itemgetter
for x in sorted(stocks, key=itemgetter(1)):
	print(x) #print AAPL\n FB\n YHOO\n AMZN\n GOOG
#official solution
from operator import itemgetter
sortedstocks = sorted(stocks.items(), key=itemgetter(1))
print(sortedstocks) #print [('YHOO', 39.28), ('FB', 76.45), ('AAPL', 99.76), ('AMZN', 305.21), ('GOOG', 520.54)]
sortedstocksreverse = sorted(stocks.items(), key=itemgetter(1), reverse=True)
print(sortedstocksreverse) #print [('GOOG', 520.54), ('AMZN', 305.21), ('AAPL', 99.76), ('FB', 76.45), ('YHOO', 39.28)]

#2. Write a Python script to add a key to a dictionary.  Sample Dictionary: {0: 10, 1: 20}.  Expected Result: {0: 10, 1: 20, 2: 30}.
initialdictionary = {0: 10, 1: 20}
initialdictionary[2] = 30
print(initialdictionary) #print {0: 10, 1: 20, 2: 30}

#3. Write a Python script to concatenate following dictionaries to create a new one.  Sample Dictionary: dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60}.  Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic123list= [dic1, dic2, dic3]
print(dic123list) #print [{1: 10, 2: 20}, {3: 30, 4: 40}, {5: 50, 6: 60}]
dic123tuple = dic1, dic2, dic3
print(dic123tuple) #print ({1: 10, 2: 20}, {3: 30, 4: 40}, {5: 50, 6: 60})
#dic123add = dic1+dic2+dic3
#print(dic123add) #error message
#official solution
dic4 = {}
for eachdic in (dic1, dic2, dic3):
	dic4.update(eachdic)
print(dic4) #print {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

#4. Write a Python script to check if a given key already exists in a dictionary.
favorite_sports = {"Ralph William":"Football", "Michael Tippett":"Basketball", "Edward Elgar":"Baseball", "Rebecca Clarke":"Netball","Ethel Smyth":"Badminton", "Frank Bridge":"Rugby"}
keycheck = "Ralph William"
for key, value in favorite_sports.items():
	if keycheck == key:
		print("{} exists".format(keycheck)) #print Ralph William exists
#no for loop
if keycheck in favorite_sports.keys():
	print("{} xist".format(keycheck)) #print Ralph William xist
else:	
	print("{} doesn't exist".format(keycheck))

#5. Write a Python program to iterate over dictionaries using for loops.
pythonglossary = {"ifelifelse": "if then elseif", "variables":"store data", "for loop":"repeat actions","functions":"call code at anytime","list":"store information"}
for key, value in pythonglossary.items():
	print("concept "+key+ " means " +value)

#6.Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). Sample Dictionary (n = 5).  Expected Output:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.
squaredictionary = {}
n = 5
for eachn in range(1,n+1):
	squaredictionary[eachn] = eachn**2
print(squaredictionary) #print {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys. Sample Dictionary {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
dictionary115 = {}
for n in range(1,16):
	dictionary115[n]=n**2
print(dictionary115) #print {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

#8. Write a Python script to merge two Python dictionaries.
alien_0 = {"color0": "green", "points0": 5}
alien_1 = {"color1": "yellow", "points1": 10}
aliens = [alien_0, alien_1]
print(aliens) #print [{'color': 'green', 'points': 5}, {'color': 'yellow', 'points': 10}]
aliensbettermerge = {**alien_0,**alien_1}
print(aliensbettermerge) #print {'color0': 'green', 'points0': 5, 'color1': 'yellow', 'points1': 10}
#also, if the keys are the same, the latter dictionary prints the keys
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
aliensonemerge = {**alien_0,**alien_1}
print(aliensonemerge) #print {'color': 'yellow', 'points': 10}
#merge three distinct keys dictionaries
alien_0 = {"color0": "green", "points1": 5}
alien_1 = {"color1": "yellow", "points2": 10}
alien_2 = {"color2": "red", "points3": 20}
aliensthreemerge = {**alien_0, **alien_1, **alien_2}
print(aliensthreemerge) #print {'color0': 'green', 'points1': 5, 'color1': 'yellow', 'points2': 10, 'color2': 'red', 'points3': 20}
