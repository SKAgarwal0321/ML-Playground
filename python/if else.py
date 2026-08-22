"""
 a = int(input("enter no. "))
for i in range(a):
    print("Hellow World")
 """

""" 
n= int(input("enter no. "))
for i in range(n+1):
    print(i)

"""

""" 
n= int(input("enter no. "))
for i in range(n, 0, -1):
    print(i)
"""
""" 
n= int(input("enter no. "))
for i in range(n, 10*n+1, n):
    print(i)
 """
""" 
#alter of table
n= int(input("enter no. "))

for i in range(1,11):
    print(f"{n}*{i} = {n*i}")
 """
""" 
n= int(input("enter no. "))

sum = 0

for i in range(1, n+1):
    sum = sum+i

print(sum)
 """

""" #factorial
n= int(input("enter no. "))

fac = 1

for i in range(1, n+1):
    fac = fac*i

print(fac)
 """
""" 
n= int(input("enter no. "))
sum= 0
for i in range(1,n):
    if n%i==0:
        sum = sum+i
        print(i)
if sum == n:
    print("perfect")
else:
    print("not perfect")
 """
""" 
n= int(input("enter no. "))
c=0
for i in range(1,n+1):
    if n%i == 0:
        c = c+1

#print(c)

if c == 2:
    print("prime")
else:
    print("not prime")
 """
""" 
#reverse string
a= input("enter string ")
b =""
#print([::-1])

for i in range(len(a)-1, -1, -1):
    b= b + a[i]
print(b)
  """

a= input("enter string ")
ch = 0
dig = 0
spch = 0
for i in a:
    if i.isdigit():
        dig += 1
    elif i.isalpha():
        ch += 1
    else:
        spch += 1
print("your digits are ",dig)
print("your character are ",ch)
print("your spetial characters are ",spch)