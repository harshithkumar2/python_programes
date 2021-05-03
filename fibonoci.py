def fib(num):
    n1 = 0
    n2 = 1

    for i in range(num):
        print(n1)
        sum = n1+n2
        n1=n2
        n2=sum



if __name__ == "__main__":
    n = int((input()))
    fib(n)