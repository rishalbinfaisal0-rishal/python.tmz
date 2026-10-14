
a = [[2,3],
    [4,5]]
b = [[2,1],
    [3.2]]

c = [[0,0],
     [0,0]]

for i in range(len(a)):
    for j in range(len(a)):
        c[i][j] = a [i][j] + b[j]
        print(c)

    