# # time

# import time 
# # print(time.ctime())
# # print(time.time())

# start = time.time()
# for i in range(1,6):
#     print(i)
#     time.sleep(1)
# end = time.time()

# print("total time :",end-start)






import time
def total_time(fun):
    def wrapper(*args,**kwargs):
        start = time.time()
        fun(*args,**kwargs)
        end = time.time()
        print("total",end-start)
    return wrapper


@total_time 
def greet(name):
    print(f"hello{name}")
greet("das")

@total_time
def addz(a,b):
    print(a+b)

addz(4,5)
@total_time
def ntime(n):
    for i in range(1,n+1):
        print(i)
        time.sleep(1)
ntime(3)