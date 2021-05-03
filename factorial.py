#loops

# def factorial(num):
#     sum = 1
#     for i in range(1,num+1):
#         sum *= i
#
#     return sum



#recursive way
def factorial(num):
    if num ==0 or num ==1:
        return 1
    else:
        return num*factorial(num-1)

if __name__ == "__main__":
    n = int((input()))
    print(factorial(n))