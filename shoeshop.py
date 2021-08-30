'''Raghu is a shoe shop owner. His shop has x number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are n number of customers who are willing to pay x(i) amount of money 
only if they get the shoe of their desired size.

Your task is to compute how much money Raghu  earned.'''

'''The first line contains x, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains n , the number of customers.
The next n lines contain the space separated values of the shoesize desired by the customer and x(i) , the price of the shoe.'''

"""SAMPLE INPUT
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

SAMPLE OUTPUT
200 """


from collections import Counter
x = int(input("number of shoes: "))
sizes = list(map(int,input("list of shoe sizes: ").split()))
sizes_d = Counter(sizes)
n = int(input("number of customers: "))
prices_l = [tuple(map(int,input().split())) for i in range(n)]
earned = 0
for s,p in prices_l:
    if s in sizes_d.keys() and sizes_d[s] > 0:
        earned = earned + p
        sizes_d[s] = sizes_d[s]-1
    else:
        continue
print(earned)