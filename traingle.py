print("1.enter the values into array\n 2.remove the values")
arr=list()
choice=int(input("enter the chioce"))
if choice == 1:
    n=int(input("enter the total"))
    for i in range(n):
        a=int(input("enter the values"))
        arr.append(a)
    b=arr.pop(len(arr)-1)
    print("deleted element is",b)
print(arr)



        
  




