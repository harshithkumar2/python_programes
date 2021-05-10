arr=list()
arr1=list()
n=int(input("enter the total for list1"))
for i in range(n):
    a=int(input("enter the number for list1"))
    arr.append(a)
n1 = int(input("enter the total for list2"))
for j in range(n1):
    a1=int(input("enter the number for list2"))
    arr1.append(a1)
arr.sort()
arr1.sort()
count = 1
size = len(arr)-1
size1 = len(arr1)-1
for k in range(len(arr)):
    if count == arr[k]:
        count = count+1
print(count)
count1=1
for l in range(len(arr1)):
    if count1 == arr1[l]:
        count1 = count1+1
print(count1)
var=arr1[0]
w=arr.pop(size)
arr.append(var)
arr1.pop(0)
arr1.append(w)
arr.sort()
arr1.sort()
print(arr)
print(arr1)

'''
enter the total for list13
enter the number for list11
enter the number for list13
enter the number for list14
enter the total for list22
enter the number for list25
enter the number for list22
2
1
[1, 2, 3]
[4, 5]
'''