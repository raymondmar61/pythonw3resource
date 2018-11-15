#33. Write a Python program to generate all sublists of a list.
from itertools import combinations
# def generatesublists(primarylist):
# 	sublist = []
# 	sublist1only = []
# 	itemcount = len(primarylist)
# 	for n in range(0,itemcount+1):
# 		# if n == 1:
# 		# 	for eachprimarylist in primarylist:
# 		# 		sublist1only.append(eachprimarylist)
# 		# 	sublist.append(sublist1only)
# 		# elif n > 1:
# 		# 	output = list(combinations(primarylist,n))
# 		# 	sublist.append(output)
# 		output = list(combinations(primarylist,n))
# 		sublist.append(output)
# 	print(sublist)
list1 = [10, 20, 30, 40]
list2 = ['X', 'Y', 'Z']
generatesublists(list1)