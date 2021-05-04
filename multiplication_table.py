def print_table(n):
    for i in range(1,11):
        print("{0} X {1} = {2}".format(n,i,n*i))

if __name__ == "__main__":
    N = int(input("Which multiplication table?"))
    print_table(N)