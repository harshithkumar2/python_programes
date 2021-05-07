def find_hcf(x,y):
    if x > y:
        small = y
    else:
        small = x

    for i in range(1,small+1):
        if ((x%i==0) and (y%i==0)):
            hcf = i
    print(hcf)


if __name__ == "__main__":
    n1 = int(input())
    n2 = int(input())
    find_hcf(n1,n2)