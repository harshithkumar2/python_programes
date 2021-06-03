arr=[1,2,3,4]
for i in range(len(arr)+1):
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            if arr[i] == 4:
                if arr[j] == 4:
                    print("true")
# if adjacent 4 the print true
