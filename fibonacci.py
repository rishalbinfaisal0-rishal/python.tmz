#fibonacci

# 0 1 1 2 3 5 8 13 21

count = int(input("Enter the count:"))
fir = 0
sec = 1
next = 0
while count > 0:
    print(fir)
    next = fir + sec
    fir = sec
    sec = next
    count = count - 1