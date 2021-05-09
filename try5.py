import math
arr=list()
n=int(input("enter the total"))
for i in range(n):
    a=int(input("enter the values"))
    arr.append(a)
q=math.floor(n/2)
s=len(arr)
first = 0
last = s-1
var=0
var1=0
temp=list()
for _ in range(q):
    if arr[first] > arr[last]:
        print("false")
    else:
        var = arr[last]
        var1=arr[first]
        temp.append(var)
        temp.append(var1)
        first = first+1
        last=last-1
        if q > first:
          print("false1")
        else:
            var = arr[last]
            
            temp.append(var)
            
            last=last-1

print(temp)
    
    
    
print(arr)
    
  
           

       
        
        
        

               
            

        
    
        



