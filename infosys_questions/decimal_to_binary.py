def dec_bin(n):

    '''# wihtout built-in function
    print("{0:b}".format(n))'''

#or with built-in function

    '''print(bin(n).replace("0b",""))'''

    #or recursive methods

    if n>=1:
        dec_bin(n//2)
    print(n%2,end="")


if __name__ == "__main__":
    n = int(input())
    dec_bin(n)