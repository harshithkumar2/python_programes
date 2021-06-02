def cap(s):
    for i in s.split():
        print(i.capitalize(),end=" ")
if __name__ == "__main__":
    s = input("Enter string")
    cap(s)