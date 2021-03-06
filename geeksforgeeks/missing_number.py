#Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.

# Input:
# N = 5
# A[] = {1,2,3,5}
# Output: 4
#
# Input:
# N = 10
# A[] = {1,2,3,4,5,6,7,8,10}
# Output: 9
#
#
# Your Task :
# You don't need to read input or print anything. Complete the function MissingNumber() that takes array and N as input  parameters and returns the value of the missing number.
#
#
# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)




def MissingNumber( array, n):
    # code here
    # array = [1]
    sum_n_no = n * (n + 1) / 2
    sum_array = sum(array)
    return int(sum_n_no - sum_array)


if __name__ == "__main__":
    arr = [1,2,3,5]
    n = 5
    ans = MissingNumber(arr,n)
    print(ans)