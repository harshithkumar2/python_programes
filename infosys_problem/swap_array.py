arr=list()
arr1=list()
n=int(input("enter the total for one"))
for i in range(n):
    a=int(input("enter the values"))
    arr.append(a)

n1=int(input("enter the total for two"))
for i in range(n1):
    a1=int(input("enter the values"))
    arr1.append(a1)

arr,arr1=arr1,arr
print(arr)
print(arr1)