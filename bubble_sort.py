#compare with each element and shift
def bubble_sort(num_arr):
    for j in range(len(num_arr)-1):
        for k in range(j+1,len(num_arr)):
            if num_arr[j] > num_arr[k]:
                num_arr[j],num_arr[k] = num_arr[k] ,num_arr[j]

    print(num_arr)


if __name__ == "__main__":
    numbers = []
    num = int(input("Enter length"))
    for _ in range(num):
        nums = int(input())
        numbers.append(nums)

    bubble_sort(numbers)