# check if a number amstrong or not ("homework")
# check if a number is amstrong or not?
# 153
# 1 ** 3 + 5 ** 3 + 3 ** 3 == 153

num = 156
org = num
total = 0
count = 0

temp = num

while temp > 0:
    temp = temp // 10
    count += 1

# print(count)

while num > 0:
    digit = num % 10
    # print(digit)
    total = total + (digit ** count)
    num = num // 10

if total == org:
    print("Armstrong number")
else:
    print("Not an Armstrong number")


# amstring
num = 153


def count(num):
    count = 0
    while num > 0:
        return count


print(count(153))


def amstring(num):
    actual_no = (num)
    while num > 0:
        b = num % 10
        c = count(actual_no)
        sum = sum + (c ** b)
        num = num//10

    print(sum)
    if actual_no:
        print("true")