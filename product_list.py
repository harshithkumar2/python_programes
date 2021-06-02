# from itertools import product
#
# a = product([1,2],[3,4])
# for i in a:
#     print(i,end=" ")
a = [1,2]
b = [3,4]
for i in a:
    for j in b:
        print((i,j), end=" ")