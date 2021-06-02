
def realsum(arr):
    sums = 0
    leng = len(mylist) - 1
    if leng == 0:
        return sums
    else:
        if 7 in mylist:
            for i in range(leng):
                if mylist[i] == 7:
                    mylist[i + 1] = 0
                    mylist[i] = 0
                else:
                    continue

        else:
            sums = sum(mylist)
            return sums

    return sum(mylist)


if __name__ == "__main__":
    mylist = [int(x) for x in input().split()]
    print(realsum(mylist))