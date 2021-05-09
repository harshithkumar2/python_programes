def add(c):
    sum=0
    for i in range(1,c+1):
        sum=sum+i
        i=i-1
    return sum



c=int(input("enter the number"))
result=add(c)
print(result)