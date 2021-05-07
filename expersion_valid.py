#pending

def valid_exp(Str):
    stack = []
    top = -1
    for i in Str:
        stack.append(i)
        top +=1



if __name__ == "__main__":
    Str = input("Enter expression")
    valid_exp(Str)