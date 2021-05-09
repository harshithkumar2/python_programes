import math
def rearrange(arr,n):
    start = 0
    last = n
    if n%2 == 0:
        size = math.floor(n / 2)
        for _ in range(size):
            val1 = arr[start]
            val2 = arr[last - 1]
            start += 1

            last -= 1
            print("{0} {1}".format(val2, val1), end=" ")
    else:
        size = math.floor(n/2) +1
        for _ in range(size):
            val1 = arr[start]
            val2 = arr[last-1]
            start += 1

            last -=1
            if start <= size -1:
                print("{0} {1}".format(val2,val1),end = " ")
            else:
                print("{0}".format(val2),end = " ")


if __name__ == "__main__":
    # n = 6
    # arr = [1,2,3,4,5,6]

    n =11
    arr = [10,20,30,40,50,60,70,80,90,100,110]
    rearrange(arr,n)