def swap(a,b):
    '''
    temp = a
    a=b
    b=temp
    print(a,b) '''

    #  or

    #python way

    '''a,b=b,a
    print(a,b)'''

    #   or without 3rd variable(xor)

    '''a = a ^ b
    b = a^b
    a=a^b
    print(a,b)'''

    #or (arithmetic operator)
    a = a+b
    b = a-b
    a = a-b
    print(a,b)

if __name__ =="__main__":
    a= int(input())
    b = int(input())
    swap(a,b)