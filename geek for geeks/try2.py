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


n=int(input("enter the total"))
arr=list()
for i in range(n):
    a=int(input("enter the values"))
    arr.append(a)
count=0
for j in range(len(arr)):
    add=0
    for k in range(j+1,len(arr)):
        add=arr[j]+arr[k]
        for y in arr:
            if add == y:
                count = count +1
print("there are",count,"triplets")
print(arr)
'''
enter the total4
enter the values1
enter the values5
enter the values3
enter the values2
there are 2 triplets
[1, 5, 3, 2]
1+2=3,2+3=5

'''