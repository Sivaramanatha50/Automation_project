import requests
# from RPA.JSON import JSON
#
# d = {"a":4, "b":5, "c": {"a":5}}
# g = JSON().get_values_from_json(d,"$..c")
#
# print(g)


#eve
#evv

def update_key(key,value):
    d = {"a":4, "b":5, "c": {"a":5}}
    keys = key.split('.')
    print('splited keys: ',keys)
    for k in keys[:-1]:
        d = d.setdefault(k,{})
    d[keys[-1]] = value
    print(d)

update_key('c.a',6)

# from collections import Counter
#
# def can_form_palindrome(s):
#     char_counts = Counter(s)
#     odd_count = sum(1 for count in char_counts.values() if count % 2 != 0)
#     print(odd_count)
#     return odd_count <= 1  # True if at most one character has an odd count
#
# # Example usage
# s = "ann"
# print(can_form_palindrome(s))  # Output: True

# n = int(input("enter number: "))
# fact = 1
#
# while(n>0):
#     fact = fact * n
#     n = n-1
# print(fact)

c = {'siva':'name',39:"age"}
f = {}

for k,v in c.items():
    f[v] = k
print(f)