def n_natural(num):
    return (n*(n+1)/2)


def n_square_natural(nums):
    return ((n*(n+1)*(2*n+1))/2)

def n_cube_natural(numss):
    return (n*(n+1)/2)**2

if __name__ == "__main__":
    n = int(input())
    print(n_natural(n))
    print(n_square_natural(n))
    print(n_cube_natural(n))