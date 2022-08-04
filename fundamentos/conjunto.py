a = {1, 2, 3}
# print(a[0]) 

a = set('abbbbcde')
print(a)

print({1, 2, 3} == {3, 2, 1, 3})

c1 = {1, 2}
c2 = {2, 3}
c1.union(c2)
c1.intersection(c2)
c1.update(c2)
print(c1)
# c2 subconjunto de c1
print(c1 >= c2)
print(c2 >= c1)

print({1, 2, 3} - {2})
c1-={2}
