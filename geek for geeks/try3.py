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

arr=list()
n=int(input("enter the total"))
for i in range(n):
    a=int(input("enter the values"))
    arr.append(a)
count=1
for j in range(len(arr)):
    if count == arr[j]:
        count=count+1
print(count)
    
print(arr)

'''
find the missing number
'''