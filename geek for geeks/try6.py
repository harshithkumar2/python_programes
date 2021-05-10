import math
n=int(input("enter the total"))
if n % 2 == 0:
    arr=list()
    for i in range(n):
        a=int(input("enter the values"))
        arr.append(a)
    q=math.floor(n/2)
    s=len(arr)
    first = 0
    last = s-1
    temp=list()
    for _ in range(q):
        var = arr[last]
        var1=arr[first]
        temp.append(var)
        temp.append(var1)
        first = first+1
        last=last-1
    print(temp)
else:
    arr=list()
    for i in range(n):
        a=int(input("enter the values"))
        arr.append(a)
    q=math.floor(n/2)
    s=len(arr)
    first = 0
    last = s-1
    temp=list()
    for _ in range(q):
        var = arr[last]
        var1=arr[first]
        temp.append(var)
        temp.append(var1)
        first = first+1
        last=last-1
        if q > first:
            continue
        else:
            var = arr[last]
            temp.append(var)
            last=last-1
    print(temp)
'''
for even
enter the total6
enter the values1
enter the values2
enter the values3
enter the values4
enter the values5
enter the values6
[6, 1, 5, 2, 4, 3]

for odd
enter the total3
enter the values1
enter the values2
enter the values3
[3, 1, 2]
'''