# decorators

# function which enhance other functions 

    # higher a function as its argument 
    # returns a functions 

def saymyname (fun):
    def wrapper(*args, **kwargs):
        print("say my name ")
        fun(*args, **kwargs)
        print("right!!!!!!!")
    return wrapper
@saymyname
def greet(name):
    print(f"hello {name}")

@saymyname
def addz(a,b):
    print(a+b)

greet("rishal")
addz(5, 6)
