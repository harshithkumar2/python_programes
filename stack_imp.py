def pushing(arr,ele):
    arr.append(ele)
    print("Element {0} inserted into the stack".format(ele))

def poping(arr):
    m = arr.pop()
    print("{0} popped from the stack".format(m))


def view(arr):
    return arr

if __name__ == "__main__":
    # n = int(input("Enter length"))
    lst = []
    # for _ in range(n):
    #     inp = int(input())
    #     lst.append(inp)

    while True:
        print("""
        1) Press 1 to push into stack
        2) Press 2 to pop from the stack
        3) Press 3 to view the stack
        4) Exit
        """)
        response = int(input())
        if response == 1:
            user_inp = int(input("Enter the element to be inserted"))
            pushing(lst , user_inp)
        elif response == 2:
            poping(lst)
        elif response == 3:
            print(view(lst))
        elif response == 4:
            break
        else:
            print("Input invalid")