#24. Write a Python program to create a dictionary from a string.  Note: Track the count of the letters from the string.  Sample string : 'w3resource'. Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)
'''
C1 C2 C3
1 5 9
2 6 10
3 7 11
'''