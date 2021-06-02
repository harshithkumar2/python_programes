def linear(arr,x):
    for i in arr:
        if i == x:
            return arr.index(i)


if __name__ == "__main__":
    arr = [2,3,6,1]
    print(linear(arr,1))