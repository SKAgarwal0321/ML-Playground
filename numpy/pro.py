import numpy as np
class1 = []
n = int(input("enter no. of test: "))
st_num = int(input("enter total no. of students: "))
# m= int(input("enter no. of students: "))
for i in range (st_num):
    print(f"enter marks of student {i+1} ",)
    marks= []
    for j in range (n):
        x= int(input(f"enter marks of {j+1} test: "))
        marks.append(x)

    class1.append(marks)
# print(class1)
a= np.array(class1).reshape(n,st_num)
print(a)
# a= np.array(sub).reshape(n,m)
# print(batch)
