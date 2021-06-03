arr=list()
x=int(input("enter the value for x"))
y=int(input("enter the value for y"))
z=int(input("enter the value for z"))
n=int(input("enter the value for n"))
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if x+y+z != n:
                arr.append([i,j,k])
print(arr)