import timeit


def rev_array_group(arr,n,k):
    start = timeit.timeit()
    lst1 = arr[:k]
    lst1.sort(reverse=True)
    lst2 = arr[k:]
    lst2.sort(reverse=True)
    lst3 = lst1+lst2
    end = timeit.timeit()
    print(lst3)
    print(end-start)

if __name__ == "__main__":
    # arr = [1,2,3,4,5]
    # n = 5
    # k =3
    arr = [5,6,8,9]
    n =4
    k=3
    rev_array_group(arr,n,k)