#using loops
def reversing(num_arr):
    reverse_num = []
    for j in range(len(num_arr)-1,-1,-1):
        reverse_num.append(num_arr[j])

        #with inbuilt functions
    # rev_list = num_arr[::-1]
    # print(rev_list)
    print("Reversed list is {0}".format(reverse_num))

if __name__ == "__main__":
    numbers = []
    num = int(input("Enter length"))
    for _ in range(num):
        nums = int(input())
        numbers.append(nums)


    reversing(numbers)