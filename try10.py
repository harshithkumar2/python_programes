arr=list()
s=input("enter the string")
arr[:]=s
index = -1
for i in range(len(arr)-1,-1,-1):
    if arr[i] == "1":
        index=i
        break
print(index)
'''
print the index if it is one or print -1
enter the string 00001
4
enter the string 0
-1
'''
