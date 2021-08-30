'''A newly opened multinational brand has decided to base their company logo on the three most
 common characters in the company name. They are now trying out various combinations
  of company names and logos based on this condition.
  Given a string s , which is the company name in lowercase letters, 
  your task is to find the top three most common characters in the string.

1] Print the three most common characters along with their occurrence count.
2] Sort in descending order of occurrence count.
3] If the occurrence count is the same, sort the characters in alphabetical order.'''

'''Sample Input 

aabbbccde

Sample Output 

b 3
a 2
c 2'''

import math
import os
import random
import re
import sys
from collections import Counter



if __name__ == '__main__':
    s = list(input("Enter the name of your company in small letters  "))
    dict1 = Counter(s)     #converts a list into dictionary like
    l1 = sorted(dict1)     #sorts a dictionary accoding to keys and returns a LIST
    dict2 = {}
    for keys in l1:
        dict2[keys] = dict1[keys]    #dict2 is a sorted dictionary accordind to its keys
    dict2 = Counter(dict2)
    l2 = list(dict2.most_common(3))  #most_common(x) is a funtion under Counter() package    
    #most_common(x) finds the most common elements by comparing the values and returns a list
    for i in range(0,len(l2)):
        print(l2[i][0]+" "+str(l2[i][1]))     #can concatenate only a string with a string not an integer
