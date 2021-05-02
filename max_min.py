
#using loops
# def max_and_min(num_arr):
#     max_ele = 0
#     min_ele = num_arr[0]
#     for j in num_arr:
#         if j < min_ele:
#             min_ele = j
#         elif j > max_ele:
#             max_ele=j
#
#     print("max number is {0} and min number is {1}".format(max_ele,min_ele))

#using buitin functions

def max_and_min(num_arr):
    max_ele = max(num_arr)
    min_ele = min(num_arr)
    print("max number is {0} and min number is {1}".format(max_ele, min_ele))

if __name__ == "__main__":
    numbers = []
    num = int(input("Enter length"))
    for _ in range(num):
        nums = int(input())
        numbers.append(nums)

    max_and_min(numbers)
