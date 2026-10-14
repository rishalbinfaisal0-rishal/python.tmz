# def countozero(n):
#     # print(n)
#     if n == 0:
#         return 0
#     return countozero(n-1)
# countozero(10)

def countozero(n):
    if n == 1:
        return 1
    return countozero(n-1)
print(countozero(5))

