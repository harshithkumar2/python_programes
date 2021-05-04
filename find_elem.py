def find_elem(num,key):
    found = 0
    for i in num:
        if i == key:
            found = 1
            index = num.index(i)

    if found:
        print("Key found at position {0}".format(index))
    else:
        print("Key not found")

if __name__ == "__main__":
    numbers = []
    num = int(input("Enter length"))
    for _ in range(num):
        nums = int(input())
        numbers.append(nums)


    key = int(input("Select key element"))

    find_elem(numbers,key)
