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
