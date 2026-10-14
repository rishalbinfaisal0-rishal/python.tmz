import random
num=random.randint(1,100)
print(num)
for i in range (1,8):
    a = int(input("enter your guss number :"))
    if a ==num:
        print("your guss is correct")
        if i == 1:
            print("your score is 70")
    elif a >num:
        print("your value is high")
    else:
        print("your value is low")
print(f"correct number is {num}")
