arr=list()
n=int(input("enter the total value "))
for i in range(n):
    a=int(input("enter the values "))
    arr.append(a)
k=0
key=int(input("enter the key "))
for e in arr:
    if key == e:
        print("key is found ",key)
        print("location is ",arr.index(key) )
print(arr)
    

