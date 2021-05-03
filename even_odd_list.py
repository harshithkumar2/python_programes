def even_odd_list(num):
    even_count = 0
    odd_count = 0
    for i in num:
        if i%2 == 0:
            even_count +=1
        else:
            odd_count += 1

    return "Even Number cout {0} Odd Number count {1}".format(even_count,odd_count)

if __name__ == "__main__":
    numbers = []
    num = int(input("Enter length"))
    for _ in range(num):
        nums = int(input())
        numbers.append(nums)

    print(even_odd_list(numbers))