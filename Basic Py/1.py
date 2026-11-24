print("Hello world")
print('You can also type in this way, not in the way belove but its ok for nums')
print({12}, "print({Not This way})")

#* Hello world
#* You can also type in this way, not in the way belove but its ok for nums
#* {12} print({Not This way})

#! print({Not This way})

write = "Hello World"
print(write)
n = 10
print(n+10)


empty_dict = {}
a = {"one": 1, "two": 2, "three": 3}
print(a["one"])
print(a.keys())
# dict_keys(['one', 'two', 'three'])

print(a.values())
# dict_values([1, 2, 3])

a.update({"four": 4})
print(a.keys())
# dict_keys(['one', 'two', 'three', 'four'])

print(a['four'])
# 4

i= 10
j= 20.00
k= "Hello"
l= True
m= [1, 2, 3]
n= (1, 2, 3)
o= {1, 2, 3}
p= {"one": 1, "two": 2, "three": 3}
q= None
r= 10 + 20j
s= b"Hello"
t= bytearray(b"Hello")
u= memoryview(b"Hello")
v= range(10)
w= frozenset({1, 2, 3})
x= complex(10, 20)
y= lambda x: x + 10
z= iter([1, 2, 3])
a= slice(1, 10, 2)
b= property(lambda self: self._x)
c= type("MyClass", (object,), {"x": 10})
d= super()
e= object()
f= staticmethod(lambda x: x + 10)
g= classmethod(lambda cls: cls.__name__)
h= enumerate([1, 2, 3])
ai= zip([1, 2, 3], ["a", "b", "c"])
aj= reversed([1, 2, 3])
ak= all([True, True, False])
al= any([True, True, False])
am= divmod(10, 3)
an= pow(2, 3)

print(type(i)/n, type(j)/n, type(k)/n, type(l)/n, type(m)/n, type(n)/n, type(o)/n, type(p)/n, type(q)/n, type(r)/n, type(s)/n, type(t)/n, type(u)/n, type(v)/n, type(w)/n, type(x)/n, type(y)/n, type(z)/n, type(a)/n, type(b)/n, type(c)/n, type(i)/n, type(j)/n, type(f)/n, type(g)/n, type(h)/n )

class counter:
    def __init__(self):
        self.value = 1
    def count_up(self):
        self.value += 1
    def count_down(self):
        self.value -= 1

    def __str__(self):
        return f"count={self.value}"

count1 = counter()
count2 = counter()

count1.count_up()
count2.count_down()

print(count1, count2)

t = (1,2,3,4)

t += (5, 6)

print(t)
