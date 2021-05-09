
def lastIndex(s):
    index = -1
    # code here
    for i in range(len(s) -1 ,-1 ,-1):
        if s[i] == "1":
            index = i
            break

    return index


if __name__ == "__main__":
    s = "111111"
    print(lastIndex(s))