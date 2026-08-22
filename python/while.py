"""
 a=1
while a<=2:
    a=a+1
    print(a)
 """

""" 
#seperate the no.
a = int(input("tell your no. "))

while a>0:
    print(a%10)
    a = a//10
"""

"""
 #reverse the no.
a = int(input("tell your no. "))
rev=0
while a>0:
    rev = rev * 10 + a % 10
    a = a//10

print(rev) 
"""
 
""" 
a = int(input("tell your no. "))
c = a
rev=0
while a>0:
    rev = rev * 10 + a % 10
    a = a//10

if c == rev:
    print("pallidrome")
else:
    print("not pallidrome")
 """    







#GAME

import random

num = random.randint(1,10)

tries = 0

while True:
    g= int(input("enter no. between 1 to 10 "))
    if num==g:
        tries += 1
        print("you are correct your tries are", tries)
        break
    
    elif num < g:
        print("go a little lower")
        tries += 1

    elif num > g:
        print("go a little higher")
        tries += 1

    else:
        tries += 1
        print("WRONG!!!!!!!!!!!!!!!!")
