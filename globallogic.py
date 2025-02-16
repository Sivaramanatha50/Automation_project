l = [[3,4,58],[709,8,9,[10,11]],[111,2]]

d = []

for i in l:
    for j in i:
        if type(j) == list:
            d.extend(j)
        else:
            d.append(j)

print(d)

# d = [
#     {"name": "Rohit", "age": 30},
#     {"name": "Abhishek", "age": 27},
#     {"name": "Akshay", "age": 28}
# ]
