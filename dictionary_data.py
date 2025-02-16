import json

d ={
    "name": "John Doe",
    "age": "30",
    "email": "john.doe@example.com",
    "is_active": "True",
    "skills": ["Python", "JavaScript", "SQL"],
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "zip": "10001"
    }
}
p = json.dumps(d)
print(p)

l = [2, 5, 3, 8, 7, 5]

# seen = set()
#
# for i in l:
#     target = 10 - i
#     if target in seen:
#        # print("target value : ",seen)
#        # print(f"Pair: ({i}, {target})")
#     seen.add(i)
l = ["aabccdee"]
s = str(str(x) for x in l)
n = list(s)
print(s)

def sorted_f(num):
    for i in range(len(num)):
        num[i] = num[i] ** 2
    return sorted(num)

print("sorted list of : ",sorted_f([25,10,30,12,55,40]))

prev =""
c = 0
out = []

for i in l:
    if i == prev:
        c += 1
    else:
        prev = i
        if c > 1:
            out.append(str(c))
        out.append(i)
        c = 1
print("hello",''.join(str(out)))
