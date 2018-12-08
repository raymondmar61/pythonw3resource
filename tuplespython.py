#https://www.w3resource.com/python-exercises/tuple/

#1. Write a Python program to create a tuple.
createtuple = (1, 2, 3, 4, 5)
print(createtuple) #print (1, 2, 3, 4, 5)

#2. Write a Python program to create a tuple with different data types.
differenttuple = (1, "one", "two", 3.14)
print(differenttuple)

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