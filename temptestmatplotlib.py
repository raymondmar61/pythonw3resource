import matplotlib.pyplot as plt
"""
plt.plot([1,2,3],[5,7,4])
plt.show()
"""

#26. Write a Python program to create a histogram from a given list of integers.
"""
xbarchart=[2,4,6,8,10]
ybarchart=[6,7,8,2,4]
xbarchart2=[1,3,5,7,9]
ybarchart2=[7,8,2,4,2]
plt.bar(xbarchart,ybarchart, label="labelbarchart", color="red")
plt.bar(xbarchart2,ybarchart2, label="labelbarchart2", color="cyan")
"""
xpopulationages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
ybins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(xpopulationages,ybins, label="labelhistogram", histtype="bar", rwidth=1.0)
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.title("Title")
plt.legend()
plt.show()

