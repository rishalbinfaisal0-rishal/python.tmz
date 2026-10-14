

# area in which it is recodnised

name = "hari"  # globaly declared


def myname():

    def nickname():  # local scope
        name = "mohan"  # local
        print(name)
        nickname()


myname()

x = 10


def twotimes():
    global x
    x = x * 2
    print(x)
twotimes()
print(x)
