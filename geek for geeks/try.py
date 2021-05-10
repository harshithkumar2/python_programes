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




arr=list()
b=int(input("enter the search number"))
n=int(input("enter the total number"))
for i in range(n):
    a=int(input("input the number"))
    arr.append(a)
for j in range(len(arr)):
    count=0
    for k in range(j+1,len(arr)):
        count=count+arr[k]
        if count+arr[j] == b:
            print("element is found from index",j+1,"to index",k+1)

'''
enter the search number5
enter the total number3
input the number1
input the number2
input the number3
element is found from index 2 to index 3
'''
