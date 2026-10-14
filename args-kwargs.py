# def add(*args): #recives as a tuple clean = list(args)
#     sum = 0
#     for i in args:
#         sum += iprint(sum)

# add(2,4,23,56,8,7,9,3,4,32,43,1,34,97,78,6,7)

def fullname(**kwargs):#recevies as a dict
    print(kwargs)
    for i in kwargs:
        full = full + kwargs[i] + ' '
    print(full)
fullname(fname="robert",mname="downie",lname="jr",fifthname="satheesh",sixthname="gane")
