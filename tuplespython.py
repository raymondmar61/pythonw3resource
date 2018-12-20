#https://www.w3resource.com/python-exercises/tuple/

#1. Write a Python program to create a tuple.
createtuple = (1, 2, 3, 4, 5)
print(createtuple) #print (1, 2, 3, 4, 5)

#2. Write a Python program to create a tuple with different data types.
differenttuple = (1, "one", "two", 3.14)
print(differenttuple) #print (1, 'one', 'two', 3.14)

#3. Write a Python program to create a tuple with numbers and print one item.
randomtuple = (9,5,48,72,354,89,30)
print(randomtuple[3]) #print 72
#official solution
#Create a tuple with numbers
tuplex = 5, 10, 15, 20, 25
print(tuplex) #print (5, 10, 15, 20, 25)
#Create a tuple of one item
tuplex = 5,
print(tuplex) #print (5,)

#4. Write a Python program to unpack a tuple in several variables.
game1, game2, game3, game4, game5 = ("Uno","Cards","X-Men","Operation","Bargain Hunter")
print(game1+game2+game3+game4+game5) #print UnoCardsX-MenOperationBargain Hunter
print(game3) #print X-Men

#5. Write a Python program to add an item in a tuple.
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
letters = ("a","r","q","g")
addletters = letters + ("p","w","s")
print(addletters) #print ('a', 'r', 'q', 'g', 'p', 'w', 's')
#adding items in a specific index
specificaddletters = addletters[1:3] + ("c","o","u") + addletters[1:3]
print(specificaddletters) #print ('r', 'q', 'c', 'o', 'u', 'r', 'q')
specificaddletters2 = addletters[0:3] + ("c","o","u") + addletters[3:]
print(specificaddletters2) #print ('a', 'r', 'q', 'c', 'o', 'u', 'g', 'p', 'w', 's')

#6. Write a Python program to convert a tuple to a string.
famousintro = ("It","was","a","dark","and","stormy","night.")
print(" ".join(famousintro)) #print It was a dark and stormy night.
#convert tuple numbers to string
favoritenumbers = (40, 100, 28, 16, 1000000)
print((" ".join(map(str,favoritenumbers)))) #print 40 100 28 16 1000000

#7. Write a Python program to get the 4th element and 4th element from last of a tuple.
manytuples = ("coke","pepsi","7-up","chocolate","vanilla","ice cream","Rite-Aid","CVS","Walgreens","hamburger","fries","shake")
print(manytuples[3]) #print chocolate
print(manytuples[-4]) #print Walgreens

#8. Write a Python program to create the colon of a tuple.
#official solution
#RM:  It's not colon.  It's clone.
from copy import deepcopy
#create a tuple
tuplex = ("HELLO", 5, [], True) 
print(tuplex) #print ('HELLO', 5, [], True) 
#make a copy of a tuple using deepcopy() function
tuplex_clone = deepcopy(tuplex)
print(tuplex_clone) #print ('HELLO', 5, [], True) 
tuplex_clone[2].append(50)
print(tuplex_clone) #print ('HELLO', 5, [50], True) 
print(tuplex) #print ('HELLO', 5, [], True) 

#9. Write a Python program to find the repeated items of a tuple.
from collections import Counter
colorlist = ("green","white","blue","blue","white","blue","green","white","green","yellow","white","blue","white","yellow","white","green","blue","red","red","white","blue","red","yellow","green","blue")
countervarible = Counter(colorlist)
print(countervarible) #print Counter({'blue': 7, 'white': 7, 'green': 5, 'red': 3, 'yellow': 3})
for key, value in countervarible.items():
	if value > 1:
		print(key, value) #print green 5\n white 7\n blue 7\n yellow 3\n red 3

#10. Write a Python program to check whether an element exists within a tuple.
phones = ("Samsung","Nokia","LG","Motorola","Blackberry")
for eachphones in phones:
	if eachphones == "Samsung":
		print("Yes "+eachphones) #print Yes Samsung
print("LG" in phones) #print True
print("Sony" in phones) #print False
#bonus
phonelist = ["Samsung","Nokia","LG","Motorola","Blackberry"]
print("LG" in phonelist) #print True
print("Sony" in phonelist) #print False

#11. Write a Python program to convert a list to a tuple.
phonelist = ["Samsung","Nokia","LG","Motorola","Blackberry"]
print(tuple(phonelist)) #print ('Samsung', 'Nokia', 'LG', 'Motorola', 'Blackberry')

#12. Write a Python program to remove an item from a tuple.
#tuples are immutable, so you can not remove elements.  Convert to list.
phonetuple = ("Samsung","Nokia","LG","Motorola","Blackberry")
print(phonetuple) #print ("Samsung","Nokia","LG","Motorola","Blackberry")
phonelist = list(phonetuple)
print(phonelist) #print ['Samsung', 'Nokia', 'LG', 'Motorola', 'Blackberry']
phonelist.remove("Motorola")
print(phonelist) #print ['Samsung', 'Nokia', 'LG', 'Blackberry']
#RM:  delete string in list use .remove().  delete integers and floats(?) use .pop()

#13. Write a Python program to slice a tuple.  RM:  separate or split or take part of a tuple
#RM tuple or string, the slice answers are the same
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
print(tuplex[3:5]) #print (5, 4)
print(tuplex[3:9:2]) #print (5, 6, 8)
print(tuplex[:6]) #print (2, 4, 3, 5, 4, 6)
print(tuplex[5:]) #print (6, 7, 8, 6, 1)
print(tuplex[:]) #print (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
print(tuplex[-8:-4]) #print (3, 5, 4, 6)
print(tuplex[-4:-8]) #print ()
print(tuplex[-4:8]) #print (7, 8) #RM:  start at -4 or count four from the right stop at index 8-1=7
print(tuplex[-7:8]) #print (5, 4, 6, 7, 8) #RM:  start at -7 or count seven from the right stop at index 8-1=7
print(tuplex[3:0:-1]) #print (5, 3, 4)

#14. Write a Python program to find the index of an item of a tuple.
sports = ("football","baseball","hockey","soccer","basketball","rugby","volleyball","baseball")
print(sports.index(("football"))) #print 0
print(sports.index(("basketball"))) #print 4

#15. Write a Python program to find the length of a tuple.
hardwarepc = ("case","hard drive","RAM","Motherboard","video card","cpu")
print(len(hardwarepc)) #print 6

#16. Write a Python program to convert a tuple to a dictionary.
hardwarepctuple = (("case",80), ("hard drive",200), ("RAM",160), ("Motherboard",180), ("video card",180), ("cpu",250))
hardwarepcdictionary = dict(hardwarepctuple)
print(hardwarepcdictionary) #print {'case': 80, 'hard drive': 200, 'RAM': 160, 'Motherboard': 180, 'video card': 180, 'cpu': 250}

#17. Write a Python program to unzip a list of tuples into individual lists.
#copied solution
hardwarepclistoftuple = [("case",80), ("hard drive",200), ("RAM",160), ("Motherboard",180), ("video card",180), ("cpu",250)]
print(list(zip(*hardwarepclistoftuple))) #print [('case', 'hard drive', 'RAM', 'Motherboard', 'video card', 'cpu'), (80, 200, 160, 180, 180, 250)]

#18. Write a Python program to reverse a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
print(tuplex[::-1]) #print (1, 6, 8, 7, 6, 4, 5, 3, 4, 2)
#official solution
reversetuplex = reversed(tuplex)
print(reversetuplex) #print <reversed object at 0x7fb22f56b7f0>
print(tuple(reversetuplex)) #print (1, 6, 8, 7, 6, 4, 5, 3, 4, 2)

#19. Write a Python program to convert a list of tuples into a dictionary.
hardwarepctuplelist = [("case",80), ("hard drive",200), ("RAM",160), ("Motherboard",180), ("video card",180), ("cpu",250)]
hardwarepcdictionary = dict(hardwarepctuplelist)
print(hardwarepcdictionary) #print {'case': 80, 'hard drive': 200, 'RAM': 160, 'Motherboard': 180, 'video card': 180, 'cpu': 250}
#official solution
xyzlist = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
xyzdictionary = {}
for key, value in xyzlist:
	xyzdictionary.setdefault(key, []).append(value)
print(xyzdictionary) #print {'x': [1, 2, 3], 'y': [1, 2], 'z': [1]}

#20. Write a Python program to print a tuple with string formatting. Sample tuple: (100, 200, 300).  Output: This is a tuple (100, 200, 300).
sampletuple = (100, 200, 300)
print("This is a tuple", sampletuple) #print This is a tuple (100, 200, 300)
print("This is a tuple {0}".format(sampletuple)) #print This is a tuple (100, 200, 300)
print("This is a tuple {}".format(sampletuple)) #print This is a tuple (100, 200, 300)

#21. Write a Python program to replace last value of tuples in a list. Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)].  Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)].
#tuples are immutable, so you can not remove elements.  Convert to list.
samplelisttuple = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
samplelistlist = []
for eachsamplelisttuple in samplelisttuple:
	eachsamplelisttuple = list(eachsamplelisttuple)
	samplelistlist.append(eachsamplelisttuple)
print(samplelistlist) #print [[10, 20, 40], [40, 50, 60], [70, 80, 90]]
for n in range(0,len(samplelistlist)):
	samplelistlist[n][2] = 100
print(samplelistlist) #print [[10, 20, 100], [40, 50, 100], [70, 80, 100]]
samplelisttuple = []
for eachsamplelistlist in samplelistlist:
	eachsamplelistlist = tuple(eachsamplelistlist)
	samplelisttuple.append(eachsamplelistlist)
print(samplelisttuple) #print [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
#quicker
samplelisttuple = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
samplelistlist = list(map(list,samplelisttuple))
print(samplelistlist) #print [[10, 20, 40], [40, 50, 60], [70, 80, 90]]
for n in range(0,len(samplelistlist)):
	samplelistlist[n][2] = 100
print(samplelistlist) #print [[10, 20, 100], [40, 50, 100], [70, 80, 100]]
samplelisttuple = list(map(tuple,samplelistlist))
print(samplelisttuple) #print [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
#official solution
samplelisttuple = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (100,) for t in samplelisttuple]) #print [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
samplelisttuple = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
for t in samplelisttuple:
	print([t[:-1]+(100,)]) #print [(10, 20, 100)]\n [(40, 50, 100)]\n [(70, 80, 100)]\n

#22. Write a Python program to remove an empty tuple(s) from a list of tuples. Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')].  Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
sampledata = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
#tuples are immutable, so you can not remove elements.  Convert to list.
sampledatalist = list(map(list,sampledata))
print(sampledatalist) #print [[], [], [''], ['a', 'b'], ['a', 'b', 'c'], ['d']]
answer = [eachsampledatalist for eachsampledatalist in sampledatalist if eachsampledatalist]
print(answer) #print [[''], ['a', 'b'], ['a', 'b', 'c'], ['d']]
answer = list(map(tuple,answer))
print(answer) #print [('',), ('a', 'b'), ('a', 'b', 'c'), ('d',)]
#RM: sampledatalist = list(map(list,sampledata)) not needed.  It seems list comprehension removes elements as if it's elements in a list.
sampledata = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
answer = [eachsampledata for eachsampledata in sampledata if eachsampledata]
print(answer) #print [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
#official solution
sampledata = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
sampledata = [eachsampledata for eachsampledata in sampledata if eachsampledata]
print(sampledata) #print [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

#23. Write a Python program to sort a tuple by its float element. Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')].  Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
sampledata = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
secondnumber = lambda sampledata: sampledata[1]
sampledata.sort(key=secondnumber, reverse=True)
print(sampledata) #print [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]

#24. Write a Python program to count the elements in a list until an element is a tuple.
thelist = ["five", 90, "grape", "blackie", "Castle Rock", (9, 5), "elephant"]
counter = 0
for eachthelist in thelist:
	if type(eachthelist) == tuple:
		break
	else:
		counter += 1
print(counter) #print 5
