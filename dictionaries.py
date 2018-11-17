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

#9. Write a Python program to iterate over dictionaries using for loops.
favorite_sports = {"Ralph William":"Football", "Michael Tippett":"Basketball", "Edward Elgar":"Baseball", "Rebecca Clarke":"Netball","Ethel Smyth":"Badminton", "Frank Bridge":"Rugby"}
for key, value in favorite_sports.items():
	print(key, value) #print Ralph William Football\n Michael Tippett Basketball\n Edward Elgar Baseball\n Rebecca Clarke Netball\n Ethel Smyth Badminton\n Frank Bridge Rugby

#10. Write a Python program to sum all the items in a dictionary.
zooanimals = {'Unicorn':'Cotton Candy House', 'Sloth':'Rainforest Exhibit',
'Bengal Tiger':'Jungle House', 'Atlantic Puffin':'Arctic Exhibit', 'Rockhopper Penguin':'Arctic Exhibit'}
print((zooanimals.items())) #print dict_items([('Unicorn', 'Cotton Candy House'), ('Sloth', 'Rainforest Exhibit'), ('Bengal Tiger', 'Jungle House'), ('Atlantic Puffin', 'Arctic Exhibit'), ('Rockhopper Penguin', 'Arctic Exhibit')])
print(len(zooanimals.items())) #print 5
#official solution
my_dict = {'data1':100,'data2':-54,'data3':247}
print(sum(my_dict.values())) #print 293

#11. Write a Python program to multiply all the items in a dictionary.
my_dict = {'data1':100,'data2':-54,'data3':247}
#print(product(my_dict.values())) #print 293
product = 1
for eachvalue in my_dict.values():
	product = product * eachvalue
print(product) #print -1333800

#12. Write a Python program to remove a key from a dictionary.
favorite_sports = {"Ralph William":"Football", "Michael Tippett":"Basketball", "Edward Elgar":"Baseball", "Rebecca Clarke":"Netball","Ethel Smyth":"Badminton", "Frank Bridge":"Rugby"}
del favorite_sports["Ethel Smyth"]
print(favorite_sports) #print {'Ralph William': 'Football', 'Michael Tippett': 'Basketball', 'Edward Elgar': 'Baseball', 'Rebecca Clarke': 'Netball', 'Frank Bridge': 'Rugby'}

#13. Write a Python program to map two lists into a dictionary.
names = ["Tom","Jerry","Dick","Matt"]
colors = ["Red","Green","Blue","Yellow"]
favoritecolors = {}
for eachnames, eachcolors in zip(names, colors):
	favoritecolors[eachnames] = eachcolors
print(favoritecolors) #print {'Tom': 'Red', 'Jerry': 'Green', 'Dick': 'Blue', 'Matt': 'Yellow'}
#official solution
favoritecolors2 = dict(zip(names, colors))
print(favoritecolors2) #print {'Tom': 'Red', 'Jerry': 'Green', 'Dick': 'Blue', 'Matt': 'Yellow'}

#14. Write a Python program to sort a dictionary by key.
favorite_sports = {"Ralph William":"Football", "Michael Tippett":"Basketball", "Edward Elgar":"Baseball", "Rebecca Clarke":"Netball","Ethel Smyth":"Badminton", "Frank Bridge":"Rugby"}
print(sorted(zip(favorite_sports.keys(), favorite_sports.values()))) #print [('Edward Elgar', 'Baseball'), ('Ethel Smyth', 'Badminton'), ('Frank Bridge', 'Rugby'), ('Michael Tippett', 'Basketball'), ('Ralph William', 'Football'), ('Rebecca Clarke', 'Netball')]
from operator import itemgetter
favorite_sports = sorted(favorite_sports.items(), key=itemgetter(0))
print(favorite_sports) #print [('Edward Elgar', 'Baseball'), ('Ethel Smyth', 'Badminton'), ('Frank Bridge', 'Rugby'), ('Michael Tippett', 'Basketball'), ('Ralph William', 'Football'), ('Rebecca Clarke', 'Netball')]
#official solution
favorite_sports = {"Ralph William":"Football", "Michael Tippett":"Basketball", "Edward Elgar":"Baseball", "Rebecca Clarke":"Netball","Ethel Smyth":"Badminton", "Frank Bridge":"Rugby"}
for key in sorted(favorite_sports):
 	print(key,favorite_sports[key]) #print Edward Elgar Baseball\n Ethel Smyth Badminton\n Frank Bridge Rugby\n Michael Tippett Basketball\n Ralph William Football\n Rebecca Clarke Netball

#15. Write a Python program to get the maximum and minimum value in a dictionary.
stocks = {"GOOG": 434, "AAPL": 325,	"FB": 54, "AMZN": 623, "F": 32, "MSFT": 549, "TWTR":29, "FIT":5}
print(max(stocks)) #print TWTR
print(min(stocks)) #print AAPL
minprice = min(zip(stocks.values(), stocks.keys()))
print(minprice) #print (5, 'FIT')
maxprice = max(zip(stocks.values(), stocks.keys()))
print(maxprice) #print (623, 'AMZN')
maxprice = max(zip(stocks.values()))
print(maxprice) #print (623,)
maxprice = max(stocks.values())
print(maxprice) #print  623
minprice = min(stocks.values())
print(minprice) #print 5
print(min(stocks.keys())) #print AAPL
print(min(stocks.values())) #print 5

#16. Write a Python program to get a dictionary from an object's fields.
#copied solution
class dictObj(object):
     def __init__(self):
         self.x = 'red'
         self.y = 'Yellow'
         self.z = 'Green'
     def do_nothing(self):
         pass
test = dictObj()
print(test.__dict__) #print {'x': 'red', 'y': 'Yellow', 'z': 'Green'}

#17. Write a Python program to remove duplicates from Dictionary.
invalidnamescolors = {"barry":"white", "bud":"black", "draymond":"green", "vanna":"white", "stone":"red", "steve":"blue", "walter":"white", "rose":"yellow", "draymond":"green"}
#keys must be unique in a dictionary
validnamescolors = {"barry":"white", "bud":"black", "draymond":"green", "vanna":"white", "stone":"red", "steve":"blue", "walter":"white", "rose":"yellow"}
print(set(validnamescolors)) #print {'steve', 'bud', 'barry', 'rose', 'draymond', 'stone', 'walter', 'vanna'}
print(set(validnamescolors.items())) #print {('walter', 'white'), ('rose', 'yellow'), ('bud', 'black'), ('stone', 'red'), ('steve', 'blue'), ('barry', 'white'), ('draymond', 'green'), ('vanna', 'white')}
noduplicates = {}
for key, value in validnamescolors.items():
	if value not in noduplicates.values():
		noduplicates[key] = value
print(noduplicates) #print {'barry': 'white', 'bud': 'black', 'draymond': 'green', 'stone': 'red', 'steve': 'blue', 'rose': 'yellow'}

#18. Write a Python program to check a dictionary is empty or not.
nopeopleages = {}
if not nopeopleages:
	print("Dictionary is empty")

#19. Write a Python program to combine two dictionary adding values for common keys.  d1 = {'a': 100, 'b': 200, 'c':300}.  d2 = {'a': 300, 'b': 200, 'd':400}.  Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
from collections import Counter
dsum = Counter(d1) + Counter(d2)
print(dsum) #print Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

#20. Write a Python program to print all unique values in a dictionary.  Sample Data: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}].  Expected Output: Unique Values:{'S005', 'S002', 'S007', 'S001', 'S009'}
sampledata = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
expectedoutput = []
for eachsampledata in sampledata:
	for key, value in eachsampledata.items():
		expectedoutput.append(value)
print(set(expectedoutput)) #print {'S001', 'S005', 'S007', 'S002', 'S009'}
#official solution
expectedoutput2 = set(value for eachsampledata in sampledata for value in eachsampledata.values()) #list comprehension.  Why am I using paranthesis instead of brackets?
print(expectedoutput2) #print {'S002', 'S007', 'S001', 'S009', 'S005'}
#or
expectedoutput3 = [value for eachsampledata in sampledata for value in eachsampledata.values()] #list comprehension.
print(set(expectedoutput3)) #print {'S002', 'S007', 'S001', 'S009', 'S005'}

#21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Sample data: {'1':['a','b'], '2':['c','d']}.  Expected Output: ac ad bc bd
sampledata = {'1':['a','b'], '2':['c','d']}
from itertools import combinations, product
list1 = ["a","b"]
list2 = ["c","d"]
print(product(sampledata["1"],sampledata["2"])) #print <itertools.product object at 0x7f8821db46c0>
print(" ".join(map(str,(product(sampledata["1"],sampledata["2"]))))) #print ('a', 'c') ('a', 'd') ('b', 'c') ('b', 'd')
print(list(product(sampledata["1"],sampledata["2"]))) #print [('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd')]
answerlist = []
for combopairs in product(sampledata["1"],sampledata["2"]):
	#product() combopairs returns a tuple.  Convert tuple to a string and append to answerlist.
	answerlist.append("".join(map(str,combopairs)))
answerlist = list(map(str,answerlist))
print(answerlist) #print ['ac', 'ad', 'bc', 'bd']
print(" ".join(map(str,answerlist))) #print ac ad bc bd
#official solution
import itertools      
d ={'1':['a','b'], '2':['c','d']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo)) #print ac\n ad\n bd\n bd

#22. Write a Python program to find the highest 3 values in a dictionary.
stocks = {"GOOG": 520.54, "FB": 76.45, "YHOO": 39.28, "AMZN": 305.21, "AAPL": 99.76, "PGE": 25, "JD": 21, "TWTR": 34, "berka": 100}
from heapq import nlargest, nsmallest
topthreestocks = nlargest(3, stocks, key=stocks.get)
print(topthreestocks) #print ['GOOG', 'AMZN', 'berka']
bottomtwostocks = nsmallest(2, stocks, key=stocks.get)
print(bottomtwostocks) #print ['JD', 'PGE']
print(nsmallest(3, stocks,  key=lambda F:F[0])) #print ['AMZN', 'AAPL', 'FB']
print(nsmallest(3, stocks,  key=lambda E:E[1])) #print ['AAPL', 'FB', JD]
print(nlargest(3, stocks,  key=lambda W:W[0])) #print ['berka', 'YHOO', 'TWTR']
print(nlargest(3, stocks,  key=lambda E:E[1])) #print ['berka', 'GOOG', 'AMZN']

#23. Write a Python program to combine values in python list of dictionaries. Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}].  Expected Output: Counter({'item1': 1150, 'item2': 300})
#RM:  copied solution.
from collections import Counter
sampledata = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result = Counter()
for d in sampledata:
    result[d['item']] += d['amount']
print(result) #print Counter({'item1': 1150, 'item2': 300})

#24. Write a Python program to create a dictionary from a string.  Note: Track the count of the letters from the string.  Sample string : 'w3resource'. Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
from collections import Counter
samplestring = "w3resource"
words = list(samplestring)
counter = Counter(words)
print(counter) #print Counter({'r': 2, 'e': 2, 'w': 1, '3': 1, 's': 1, 'o': 1, 'u': 1, 'c': 1})
#official solution
from collections import defaultdict, Counter
my_dict = {}
for letter in samplestring:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict) #print {'o': 1, '3': 1, 's': 1, 'r': 2, 'w': 1, 'u': 1, 'e': 2, 'c': 1}

#25. Write a Python program to print a dictionary in table format.
#official solution
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)
'''
C1 C2 C3
1 5 9
2 6 10
3 7 11
'''

#26. Write a Python program to count the values associated with key in a dictionary.  Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]  Expected result: Count of how many dictionaries have success as True
sampledata = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
truecounter = 0
for eachsampledata in sampledata:
	if eachsampledata["success"] is True:
		truecounter += 1
print(truecounter) #print 2
#official solution
print(sum(d['success'] for d in sampledata)) #print 2

#27. Write a Python program to convert a list into a nested dictionary of keys.
#RM:  copied solution.  I understood after seeing the answer.
num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]	
    #print(current) #print {}\n{}\n{}\n{}\n
print(new_dict) #print {1: {2: {3: {4: {}}}}}

#28. Write a Python program to sort a list alphabetically in a dictionary.
#RM:  dictionary comprehension
num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
sortednum = {}
for key, value in num.items():
	sortednum[key] = (sorted(value))
print(sortednum) #{'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}
#official solution
sorted_dict = {x: sorted(y) for x, y in num.items()}
print(sorted_dict) #print {'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}

#29. Write a Python program to remove spaces from dictionary keys.
spaceskey = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
nospaceskey = {}
for key, value in spaceskey.items():
	key = key.replace(" ","")	
	nospaceskey[key] = value
print(nospaceskey) #print {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']}
#official solution
student_dict = {x.translate({32: None}): y for x, y in spaceskey.items()}
print("New dictionary: ",student_dict) #print New dictionary:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']}

#30. Write a Python program to get the top three items in a shop. Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}.  Expected Output: item4 55 item1 45.5 item3 41.3
sampledata = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
from heapq import nlargest
topthreesampledata = nlargest(3, sampledata, key=sampledata.get)
for eachtopthreesampledata in topthreesampledata:
	print(eachtopthreesampledata,sampledata[eachtopthreesampledata]) #print item4 55\n item1 45.5\n item3 41.3
#official solution
from heapq import nlargest
from operator import itemgetter
items = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
for name, value in nlargest(3, items.items(), key=itemgetter(1)):
    print(name, value) #print item4 55\n item1 45.5\n item3 41.3

#31. Write a Python program to get the key, value and item in a dictionary.
#copied solution
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("key  value  count")
for count, (key, value) in enumerate(dict_num.items(), 1):
    print(key,'   ',value,'    ', count)
'''
key  value  count
1     10      1
2     20      2
3     30      3
4     40      4
5     50      5
6     60      6
'''
favorite_sports = {"Ralph William":"Football", "Michael Tippett":"Basketball", "Edward Elgar":"Baseball", "Rebecca Clarke":"Netball","Ethel Smyth":"Badminton", "Frank Bridge":"Rugby"}
print("key  value  count")
for count, (key, value) in enumerate(favorite_sports.items(), 1):
    print(key,'   ',value,'    ', count)
'''
key  value  count
Ralph William     Football      1
Michael Tippett     Basketball      2
Edward Elgar     Baseball      3
Rebecca Clarke     Netball      4
Ethel Smyth     Badminton      5
Frank Bridge     Rugby      6
'''

#32. Write a Python program to print a dictionary line by line.
#copied solution
students = {'Alex':{'class':'V','rolld_id':2}, 'Pam':{'class':'V','roll_id':3}, 'Ann':{'class':'V','roll_id':4}, 'Jack':{'class':'V','roll_id':5}, 'Kelvin':{'class':'V','roll_id':7}, 'Otto':{'class':'V','roll_id':9}, 'Timmy':{'class':'V','roll_id':16}}
for key in students:
	print(key) #print Alex\n Pam\n . . . Otto\n Timmy  RM:  print each key on its own line
for value in students:
	print(value) #print Alex\n Pam\n . . . Otto\n Timmy  RM:  print each key on its own line
for key in students.items():
	print(key) #print ('Alex', {'class': 'V', 'rolld_id': 2})\n . . . ('Timmy', {'class': 'V', 'roll_id': 16})  RM:  print each key and its dictionary on its own line as a tuple
for value in students.items():
	print(value) #print ('Alex', {'class': 'V', 'rolld_id': 2})\n . . . ('Timmy', {'class': 'V', 'roll_id': 16})  RM:  print each key and its dictionary on its own line as a tuple
for key, value in students.items():
	print(key, value) #print 'Alex' {'class': 'V', 'rolld_id': 2}\n . . . 'Timmy' {'class': 'V', 'roll_id': 16}  RM:  print each key and its value as dictionary on its own line
for key in students:
	print(key+":") #print Alex:
	for eachvalue in students[key]:
		print(eachvalue) #print class ... roll_id
		print(students[key][eachvalue]) #print V ... 2
		print(eachvalue,":",students[key][eachvalue]) #print class: V ... roll_id: 2
'''
Alex:
class
V
class :  V
rolld_id
2
rolld_id :  2
Pam:
class
V
class :  V
roll_id
3
roll_id :  3
Ann:
class
V
class :  V
roll_id
4
roll_id :  4
'''

#33. Write a Python program to check multiple keys exists in a dictionary.
#copied solution
#RM:  what is the purpose?
student = {'name': 'Alex', 'class': 'V', 'roll_id': '2'}
print(student.keys() >= {'class', 'name'}) #print True
print(student.keys() >= {'name', 'Alex'}) #print False
print(student.keys() >= {'roll_id', 'name'}) #print True

#34. Write a Python program to count number of items in a dictionary value that is a list.
num = {'the1': [2, 3, 1, 4, 5, 7], 'the2': [5, 1, 2, 200], 'the3': [3, 2, 4, 33, 44, 55, 66, 77]}
for key, value in num.items():
	print(key,len(value)) #print the1 6\n the2 4\n the3 8

#35. Write a Python program to sort Counter by value.  Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}.  Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
sampledata =  {'Math':81, 'Physics':83, 'Chemistry':87}
print(sorted(zip(sampledata.values(), sampledata.keys()))) #print [(81, 'Math'), (83, 'Physics'), (87, 'Chemistry')]
sampledatareverse = sorted(sampledata.items(), key=itemgetter(1), reverse=True)
print(sampledatareverse) #print [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
sampledatakeyforward = sorted(sampledata.items(), key=itemgetter(0), reverse=False)
print(sampledatakeyforward) #print [('Chemistry', 87), ('Math', 81), ('Physics', 83)]
#official solution
from collections import Counter
x = Counter({'Math':81, 'Physics':83, 'Chemistry':87})
print(x.most_common())

#36. Write a Python program to create a dictionary from two lists without losing duplicate values.  Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3].  Expected Output: defaultdict(<class 'set'>, {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': {3}, 'Class-V': {1}})
#copied solution
from collections import defaultdict
list1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
list2 = [1, 2, 2, 3]
temp = defaultdict(set)
for c, i in zip(list1, list2):
    temp[c].add(i)
print(temp) #print defaultdict(<class 'set'>, {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}})

#37. Write a Python program to replace dictionary values with their sum.
num = {'the1': [2, 3, 1, 4, 5, 7], 'the2': [5, 1, 2, 200], 'the3': [3, 2, 4, 33, 44, 55, 66, 77]}
for key in num:
	numsum = 0
	for eachvalue in num[key]:
		numsum = numsum + eachvalue
	num[key] = []
	num[key].append(numsum)
print(num) #print {'the1': [22], 'the2': [208], 'the3': [284]}
#official solution
def sum_math_v_vi_average(list_of_dicts):
    for d in list_of_dicts:
        n1 = d.pop('V')
        n2 = d.pop('VI')
        d['V+VI'] = (n1 + n2)/2
    return list_of_dicts 
student_details= [{'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82}, {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74}, {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}]
print(sum_math_v_vi_average(student_details)) #print [{'subject': 'math', 'id': 1, 'V+VI': 76.0}, {'subject': 'math', 'id': 2, 'V+VI': 73.5}, {'subject': 'math', 'id': 3, 'V+VI': 80.5}]

#38. Write a Python program to match key values in two dictionaries. Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}.  Expected output: key1: 1 is present in both x and y.
#copied solution
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
for (key, value) in set(x.items()) & set(y.items()):
    print('%s: %s is present in both x and y' % (key, value)) #print key1: 1 is present in both x and y 