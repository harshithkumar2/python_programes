#compare current element with previous all elements
def insertion_sort(num_arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(num_arr)):

        key = num_arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < num_arr[j]:
            num_arr[j + 1] = num_arr[j]
            j -= 1
        num_arr[j + 1] = key

    print(num_arr)

if __name__ == "__main__":
    numbers = []
    num = int(input("Enter length"))
    for _ in range(num):
        nums = int(input())
        numbers.append(nums)

    insertion_sort(numbers)