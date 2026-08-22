""" 
 """
""" 
#1. Sum of a list — Write a loop to calculate the sum of all numbers in a list without using sum().

sum = 0 
for j in range(n):
    sum = sum + l[j]
print(sum)
 """

#2. FizzBuzz — Print numbers 1–30. For multiples of 3 print "Fizz", multiples of 5 print "Buzz", both print "FizzBuzz"

""" 
for j in l:
    if j%3 == 0:
        print(j, "Fizz")
    elif j%5 == 0:
        print(j, "Buzz")
    elif j%15 == 0:
        print(j, "FizzBuzz")
    else:
        print(j, "NIKAL YAHA SE")
 """

# 3.Reverse a list — Use a loop to reverse a list without using .reverse() or slicing.
""" 
for i in range(len(l) // 2):
    opposite = len(l) - 1 - i
    l[i], l[opposite] = l[opposite], l[i]

print(l)  
"""

# 4. Find the maximum — Loop through and find the largest number without using max().
""" 
great= l[0]
for j in range(len(l)):
    if l[j] > l[0]:
        great= l[j]
        print("greatest is = ", great)
"""

# 5.Flatten a nested list — Convert [[1, 2], [3, 4], [5, 6]] into [1, 2, 3, 4, 5, 6] using nested loops
""" 
l = [[1, 2], [3, 4], [5, 6]]
l1= []

for i in l:
    for j in i:
        l1.append(j)
    #     print(l1)
    # print(l1)
print(l1)
"""

# 5. Multiplication table — Print a 5×5 multiplication table using nested for loops.
""" 
for i in range(1,6):
    for j in range(1,6):
        print(i*j, end="/t")
 """

# 6.Count word frequency — Given a sentence, count how many times each word appears using a loop 
""" 
sentance= input("enter the swntance you want ")
words = sentance.split()
# word = input("enter the word you want ")
count = 0
for i in words:
    if i in count:
        count[i] = count+1
    else:
        count = 1
print(count)
# print(f"the word '{word}' occured {count} times in the given sentanse")
 """

# 7. Manual dot product — Given two vectors a = [1, 2, 3] and b = [4, 5, 6], compute their dot product using a loop (this is core to neural networks!).
""" 
# a = [1, 2, 3]
# b = [4, 5, 6]
a= []
# n = int(input("enter no. of elements you want in list a: "))

for i in range(3):
    x= int(input("enter no. you want in list: "))
    a.append(x)
print("your list is: ", a)

b= []
# m  = int(input("enter no. of elements you want in list b: "))

for i in range(3):
    x= int(input("enter no. you want in list: "))
    b.append(x)
print("your list is: ", b)

s= 0
for i in range(3):
    x=a[i]*b[i]
    s = s+x
print("dot product is = ",s)
 """

# 8.Normalize a list — Loop through [10, 20, 30, 40, 50] and normalize each value to a 0–1 range using:normalized = (x - min) / (max - min)

# l = [10, 20, 30, 40, 50]

l= []
n = int(input("enter no. of elements you want in list: "))

for i in range(n):
    x= int(input("enter no. you want in list: "))
    l.append(x)
print("your list is: ", l)

max= l[0]
for j in range(len(l)):
    if l[j] > max:
        max = l[j]

min = l[0]
for mins in range(len(l)):
    if l[mins] < min:
        min = l[mins]

for x in l:
    x = x-min
    a = max-min
    normalized= x/a
# round(): to get req decimals
    print(round(normalized , 2))
     
