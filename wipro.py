
# l = [i for i in range(100) if all( i % j !=0 for j in range(2,i))]
# print(l)

# t = (1,2,3,[4,5])
# print(id(t[3]))
# #t = (1,2,3,[4,,5,6])
# ind = t[-1]
# ind.append(6)
# print(ind)
# print(t)
# print(id(t[3]))

# a = ['2','5','3','2','10']
# # ['2','3','5','10']
# l = [int(i) for i in a]
# n = len(l)
#
# for i in range(n):
#     for j in range(0,n-i-1):
#         if a[j] > a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
#
# print(l)
# l2 = []
# for i in l:
#     if i not in l2:
#         l2.append(i)
# v = [str(i) for i in l2]
# k = len(v)
#
# for i in range(k):
#     for j in range(0,k-i-1):
#

class A:
    def __init__(self,name,):
        self.name = name

        print("class A",self.name)


class B(A):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__(self.name)
        print("class B",self.name,self.age)


# class C:
#     def __init__(self):
#         print("class C")

obj = B('siva',23)

# try:
#     print(2/0)
# except Exception as e:
#     print(e)

def servicetax(fun):
    def innrer(*args):
        amt = fun(*args)
        namt = amt + amt * 0.07
        return namt
    return innrer

@servicetax
def customer(a):
    return a
print(customer(100))


