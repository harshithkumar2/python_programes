arr=list()
n=int(input("enter the total"))
k=int(input("enter teh size"))
for i in range(n):
    a=int(input("enter the values"))
    arr.append(a)
left = 0
right = k-1
left1 =  k
right1=len(arr)-1
while(True):
    arr[left],arr[right]=arr[right],arr[left]
    arr[left1],arr[right1]=arr[right1],arr[left1]
    break
print(arr)


'''
enter the total5
enter teh size3
enter the values1
enter the values2
enter the values3
enter the values4
enter the values5
[3, 2, 1, 5, 4]
enter the total4
enter teh size3
enter the values5
enter the values6
enter the values8
enter the values9
[8, 6, 5, 9]
'''  