def swap(num):
    size=len(num)
    temp=num[0]
    num[0]=num[size-1]
    num[size-1]=temp
    return num
arr=list()
n=int(input("enter the totral"))
for i in range(n):
    a=int(input("enter the values"))
    arr.append(a)
result=swap(arr)
print(result)