def adjacent(arr):
    for i in range(len(arr)-1):
        if 4 in arr:
            if arr[i] == 4:
                if arr[i+1] == 4:
                    return True
                else:
                    return False
            elif arr[len(arr)-1] == 4 and arr[len(arr)-2] !=4:
                return False

        else:
            return False

if __name__ == "__main__":
    arr = [1,4,2,3,4]
    print(adjacent(arr))