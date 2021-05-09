def fib(n):
    a=0
    b=1
    if n == 1:
        print("fibbonaci no. is ",a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print("fibbonaci no. is ",c)




n=int(input("enter the number "))
fib(n)
