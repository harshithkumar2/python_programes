def findHcf(a,b):
    hcf = 0
    for i in range(2,b+1):
        if a%i == 0 and b%i == 0:
            hcf = i
        else:
            continue
    print(hcf)
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    findHcf(n,m)