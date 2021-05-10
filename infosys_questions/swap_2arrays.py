def swap_arr(arr1,arr2,arr3):
    print("array1 before swap {0}".format(arr1))
    print("array2 before swap {0}".format(arr2))

    for i in range(len(arr1)):
        arr1[i],arr2[i] = arr2[i],arr1[i]

    print("array1 after swap {0}".format(arr1))
    print("array2 after swap {0}".format(arr2))


if __name__ =="__main__":
    arr1 = [1,2,3,4,5]
    arr2 = [6,7,8,9,0]
    arr3 = []
    swap_arr(arr1,arr2,arr3)