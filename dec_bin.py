def dec_bin(n):
    lst = []
    while n >=1:
        c = n%2
        n = n //2
        lst.append(c)

    print(lst[::-1])
if __name__  == "__main__":
    a = int(input())
    dec_bin(a)
