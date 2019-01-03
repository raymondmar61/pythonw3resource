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
