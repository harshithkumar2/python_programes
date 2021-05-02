def seperate(num_arr):
    neg_list = []
    pos_list = []
    for j in num_arr:
        if j < 0:
            neg_list.append(j)
        else:
            pos_list.append(j)

    print("Negative number list {0} and positive number list {1}".format(neg_list,pos_list))


if __name__ == "__main__":
    numbers = []
    num = int(input("Enter length"))
    for _ in range(num):
        nums = int(input())
        numbers.append(nums)

    seperate(numbers)