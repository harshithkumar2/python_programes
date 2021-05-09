def triangle(n):
    for i in range(0,n):
        for j in range(0,i):
            print("*")


if __name__ == "__main__":
    n = int(input("Enter size"))
    triangle(n)