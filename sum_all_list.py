#using loop

def sums_list(num_arr):
    sums = 0
    for j in num_arr:
        sums += j

    #using inbuilt function


    # print(sum(num_arr))

    print(sums)

if __name__ == "__main__":
    numbers = []
    num = int(input("Enter length"))
    for _ in range(num):
        nums = int(input())
        numbers.append(nums)

    sums_list(numbers)