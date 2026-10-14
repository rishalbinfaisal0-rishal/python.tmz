# x = "apple"

# for i in range(1,6):
#     print(i)
#     for k in range(i,6):
#         print(" ",end=" ")


word = "apple"

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")

    for k in range(i):
        print(word[5 - i + k], end=" ")

    print()




    #     e
    #    l e
    #   p l e
    #  p p l e
    # a p p l e