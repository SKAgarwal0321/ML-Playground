s = {1, 2, 3, 4, 5}
b= {4, 5, 6, 7, 9,}
s.add(8)#to add somethig
s.remove(2)
s.discard(5)
p= s.pop()
a= s.union(b)
a= s|b #union
c= s.intersection(b)
d= a&b #intersection
e= s.difference(b)
e= s-b #diffrensce
print(s)
print(a)
print(c)
print(d)