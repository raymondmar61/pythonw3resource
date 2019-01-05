#https://www.w3resource.com/python-exercises/sets/

#1. Write a Python program to create a set.
gameset = set(["Sorry","X-Men","Kingdomino","Operation"])
print(gameset) #print {'X-Men', 'Sorry', 'Kingdomino', 'Operation'}

#2. Write a Python program to iteration over sets.
gameset = set(["Sorry","X-Men","Kingdomino","Operation"])
for eachgameset in gameset:
	print(eachgameset) #print Operation\n X-Men\n Kingdomino\n Sorry
#bonus list comprehension convert list to set
gamesetiterate = [eachgameset for eachgameset in gameset]
print(gamesetiterate) #print ['Sorry', 'X-Men', 'Kingdomino', 'Operation'] #convert set to list

#3. Write a Python program to add member(s) in a set.
gameset = set(["Sorry","X-Men","Kingdomino","Operation"])
gameset.add("Clue")
gameset.add("Monopoly")
print(gameset) #print {'Clue', 'Kingdomino', 'X-Men', 'Operation', 'Sorry', 'Monopoly'}
gameset.update(["Settlers Of Catan","Puerto Rico"])
print(gameset) #print {'Settlers Of Catan', 'Sorry', 'Monopoly', 'Puerto Rico', 'Operation', 'Kingdomino', 'Clue', 'X-Men'}

#4. Write a Python program to remove item(s) from set
gameset = set(["Sorry","X-Men","Kingdomino","Operation"])
gameset.add("Clue")
gameset.add("Monopoly")
print(gameset) #print {'Clue', 'Kingdomino', 'X-Men', 'Operation', 'Sorry', 'Monopoly'}
gameset.remove("Monopoly")
gameset.remove("Clue")
print(gameset) #print {'X-Men', 'Sorry', 'Operation', 'Kingdomino'}
gameset.pop() #RM:  .pop() removes an item from a set randomly
print(gameset) #print {'X-Men', 'Operation', 'Kingdomino'} or {'Sorry', 'Kingdomino', 'X-Men'} or ?

#5. Write a Python program to remove an item from a set if it is present in the set.
gameset = set(["Sorry","X-Men","Kingdomino","Operation"])
gameset.add("Clue")
gameset.add("Monopoly")
print(gameset) #print {'Clue', 'Kingdomino', 'X-Men', 'Operation', 'Sorry', 'Monopoly'}
gameset.remove("Monopoly")
gameset.remove("Clue")
print(gameset) #print {'X-Men', 'Sorry', 'Operation', 'Kingdomino'}
gameset.discard("Dominion") #RM:  solution is using setname.discard()
print(gameset) #print {'X-Men', 'Sorry', 'Operation', 'Kingdomino'}

#6. Write a Python program to create an intersection of sets.
colors1 = set(["black","white","blue","green","yellow","orange"])
colors2 = set(["red","orange","yellow","green","blue","indigo"])
colors3 = colors1.intersection(colors2)
print(colors3) #print {'green', 'orange', 'yellow', 'blue'}
#official solution
colors3official = colors1 & colors2
print(colors3official) #print {'green', 'orange', 'yellow', 'blue'}
#addinum
colors12 = set(["teal","brown","white","blue","green"])
colors4 = colors1 & colors2 & colors12
print(colors4) #print {'blue','green'}

#7. Write a Python program to create a union of sets.
colors1 = set(["black","white","blue","green","yellow","orange"])
colors2 = set(["red","orange","yellow","green","blue","indigo"])
colors3 = colors1.union(colors2)
print(colors3) #print {'red', 'indigo', 'yellow', 'white', 'blue', 'black', 'orange', 'green'}
colors12 = set(["teal","brown","white","blue","green"])
colors4 = colors1 | colors2 | colors12
print(colors4) #print {'indigo', 'red', 'brown', 'white', 'yellow', 'orange', 'teal', 'green', 'blue', 'black'}

#8. Write a Python program to create set difference.
colors1 = set(["black","white","blue","green","yellow","orange"])
colors2 = set(["red","orange","yellow","green","blue","indigo"])
colors3a = colors1.difference(colors2) 
print(colors3a) #print {'black', 'white'}
print(colors1 - colors2) #print {'black', 'white'}
colors3b = colors2.difference(colors1)
print(colors3b) #print {'red', 'indigo'}
print(colors2 - colors1) #print {'red', 'indigo'}
colors12 = set(["teal","brown","white","blue","green"])
colors4a = colors1 - colors2 - colors12
print(colors4a) #print {'black'}
colors4b = colors12 - colors2 - colors1
print(colors4b) #print {'brown', 'teal'}
colors4c = colors2 - colors12 - colors1
print(colors4c) #print #print {'red', 'indigo'}

#9. Write a Python program to create a symmetric difference.
#https://www.programiz.com/python-programming/methods/set/symmetric_difference
#The symmetric difference of two sets A and B is the set of elements which are in either of the sets A or B but not in both.
colors1 = set(["black","white","blue","green","yellow","orange"])
colors2 = set(["red","orange","yellow","green","blue","indigo"])
colors3 = colors1.symmetric_difference(colors2)
print(colors3) #print {'white', 'red', 'indigo', 'black'}
print(colors1 ^ colors2) #print {'white', 'black', 'indigo', 'red'}
colors12 = set(["teal","brown","white","blue","green"])
print(colors1 ^ colors2 ^ colors12) #print {'indigo', 'teal', 'red', 'blue', 'brown', 'green', 'black'}
print(colors12 ^ colors1 ^ colors2) #print {'indigo', 'teal', 'red', 'blue', 'brown', 'green', 'black'}
print(colors2 ^ colors12 ^ colors1) #print {'indigo', 'teal', 'red', 'blue', 'brown', 'green', 'black'}

#10. Write a Python program to issubset and issuperset.
#https://www.programiz.com/python-programming/methods/set/issubset The issubset() method returns True if all elements of a set are present in another set.
colors1 = set(["black","white","blue","green","yellow","orange"])
colors2 = set(["red","orange","yellow","green","blue","indigo"])
colors3 = colors1.issubset(colors2)
print(colors3) #print False
print(colors2.issubset(colors1)) #print False
colors2incolors1 = set(["white","orange"])
print(colors2incolors1.issubset(colors1)) #print True
print(colors2incolors1 <= colors1) #print True
print(colors1.issubset(colors2incolors1)) #print False
print(colors1 <= colors2incolors1) #print False
print("\n")
#https://www.programiz.com/python-programming/methods/set/issuperset The issuperset() method returns True if a set has every elements of another set (passed as an argument).
colors1 = set(["black","white","blue","green","yellow","orange"])
colors2 = set(["red","orange","yellow","green","blue","indigo"])
colors3 = colors1.issuperset(colors2)
print(colors3) #print False
print(colors2.issuperset(colors1)) #print False
colors2incolors1 = set(["white","orange"])
print(colors2incolors1.issuperset(colors1)) #print False
print(colors2incolors1 >= colors1) #print False
print(colors1.issuperset(colors2incolors1)) #print True
print(colors1 >= colors2incolors1) #print True

#11. Write a Python program to create a shallow copy of sets.  Note : Shallow copy is a bit-wise copy of an object. A new object is created that has an exact copy of the values in the original object.
#https://www.geeksforgeeks.org/set-copy-python/
colors1 = set(["black","white","blue","green","yellow","orange"])
colors1copy = colors1.copy()
print(colors1copy) #print {'blue', 'orange', 'black', 'white', 'green', 'yellow'}

#12. Write a Python program to clear a set.
colors1 = set(["black","white","blue","green","yellow","orange"])
print(colors1) #print {'orange', 'black', 'yellow', 'green', 'white', 'blue'}
colors1.clear()
print(colors1) #print set()

#13. Write a Python program to use of frozensets.
#https://www.programiz.com/python-programming/methods/built-in/frozenset
#The frozenset() method returns an immutable frozenset object initialized with elements from the given iterable.  Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time, elements of frozen set remains the same after creation.
colors1 = set(["black","white","blue","green","yellow","orange"])
print(colors1) #print {'orange', 'black', 'yellow', 'green', 'white', 'blue'}
colors1frozen = frozenset(colors1)
print(colors1frozen) #print frozenset({'green', 'yellow', 'white', 'orange', 'blue', 'black'})
#official solution
x = frozenset([1, 2, 3, 4, 5])
y = frozenset([3, 4, 5, 6, 7])
#use isdisjoint(). Return True if the set has no elements in common with other. 
print(x.isdisjoint(y)) #print False
#use difference(). Return a new set with elements in the set that are not in the others.
print(x.difference(y)) #print frozenset({1, 2}) 
#new set with elements from both x and y
print(x | y) #print frozenset({1, 2, 3, 4, 5, 6, 7}) 

#14. Write a Python program to find maximum and the minimum value in a set.
colors1 = set(["black","white","blue","green","yellow","orange"])
print(min(colors1)) #print black
print(max(colors1)) #print yellow

#15. Write a Python program to find the length of a set.
colors1 = set(["black","white","blue","green","yellow","orange"])
print(len(colors1)) #print 6