import random

# # from random import random


# print(random.randint(1,10))

# fruits = ("apple","orange","mango","mango","pinapple","grapes","watermelone")

# print(random.choice(fruits))
guss = input(("head or tail :-"))
coin = ("head","tail")
print(random.choice(coin))
if guss == coin:
    print("correct")
else:
    print("false")

