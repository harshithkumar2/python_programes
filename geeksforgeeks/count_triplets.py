#Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.

# Input:
# N = 4
# arr[] = {1, 5, 3, 2}
# Output: 2
# Explanation: There are 2 triplets:
# 1 + 2 = 3 and 3 +2 = 5
#
#
# Input:
# N = 3
# arr[] = {2, 3, 4}
# Output: 0
# Explanation: No such triplet exits
#
#
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function countTriplet() which takes the array arr[] and N as inputs and returns the triplet count
#
# Expected Time Complexity: O(N2)
# Expected Auxiliary Space: O(1)
#
# Constraints:
# 1 ≤ N ≤ 103
# 1 ≤ arr[i] ≤ 105

def countTriplet( arr, n):
    # code here
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            sums = arr[i] + arr[j]
            for k in range(len(arr)):
                if sums == arr[k]:
                    count += 1

    return count


if __name__ == "__main__":
    #arr = [1,5,3,2]
    arr = [2,3,4]
    n = len(arr)
    ans = countTriplet(arr,n)
    print(ans)