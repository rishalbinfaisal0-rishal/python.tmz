# lazy iterable


# value on demand

z = ["mohan",2,3,4,5,6,5,4,6,7,7,5]

def mydata():
    yield "mohan"
    yield "fdn"
    yield "modvn"
    yield "mohe"
    yield "mfkwef"
    yield "mohan"
    yield "mokf"
    yield "ryie"
    yield "two"

a = mydata()
print(next(a))
print(next(a))
for i in a :
    print(i)

    def infiz():
        i = 1
        while True:
            i = 1
            while True:
                i = i + 2
                yield i


infinite = infiz()

for i in infinite:
    print(i)

    import sys

a = []
for i in range (1,100000):
    a.append(i)

def million():
    for i in range(1,10000):
        yield i 
b = million()
print(sys.getsizeof(a))
print(sys.getsizeof(b))