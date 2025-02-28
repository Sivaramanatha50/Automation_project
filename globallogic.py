l = [[3,4,58],[709,8,9,[10,11]],[111,2]]

d = []

for i in l:
    for j in i:
        if type(j) == list:
            d.extend(j)
        else:
            d.append(j)

print(d)
d = [
    {"name": "Rohit", "age": 30},
    {"name": "Abhishek", "age": 32},
    {"name": "Akshay", "age": 28}
]
l = sorted(d, key=lambda x:x['age'])
print("sorted: ",l)
n = len(d)

for i in range(n):
    for j in range(0,n-i-1):
        if d[j]['age'] > d[j+1]['age']:
            d[j],d[j+1] = d[j+1],d[j]
print(d)

l = [1,2,3,4]
l2 = [2,4,5]
l3 = []

for i in l:
    if i in l2:
        print(i)
for i in l,l2:
    for j in i:
        if j not in l3:
            l3.append(j)
print(l3)