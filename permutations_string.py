def permutations(s,size):
    n = itertools.permutations(s,size)
    for i in n:
        print("".join(i),end=" ")

if __name__ == "__main__":
    import itertools
    s = input("Enter string")
    size = int(input("Enter length"))
    permutations(s,size)