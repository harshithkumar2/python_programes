# Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.
#
# EX 1) Input:
# N = 5, S = 12
# A[] = {1,2,3,7,5}
# Output: 2 4
# Explanation: The sum of elements
# from 2nd position to 4th position
# is 12.
#
# EX 2) N = 10, S = 15
# A[] = {1,2,3,4,5,6,7,8,9,10}
# Output: 1 5
# Explanation: The sum of elements
# from 1st position to 5th position
# is 15.
#
# Your Task:
# You don't need to read input or print anything. The task is to complete the function subarraySum() which takes arr, N and S as input parameters and returns a list containing the starting and ending positions of the first such occurring subarray from the left where sum equals to S. The two indexes in the list should be according to 1-based indexing. If no such subarray is found, return -1.



def subArray(arr,n,s):
    lstt = []
    for i in range(len(arr)):
        sum = 0
        for j in range(i + 1, len(arr)):
            sum += arr[j]
            if sum + arr[i] == s:
                lstt.append(i+1)
                lstt.append(j+1)

    print("{0} {1}".format(lstt[0],lstt[1]))


if __name__ == "__main__":
    n = 10
    s = 15
    arr = [1,2,3,4,5,6,7,8,9,10]
    subArray(arr,n,s)
