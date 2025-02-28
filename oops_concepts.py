
class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_a(self):
        print("class A variable",self.name)

class B(A):

    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id

    def display_b(self):
        print("class B variable",self.name,self.age,self.id)

obj = B("sivaram",30,26)
obj.display_a()
obj.display_b()

l = [0,1,0,1,1,0]

n = len(l)

for i in range(n):
    for j in range(0,n-i-1):
        if l[j] < l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
print(l)