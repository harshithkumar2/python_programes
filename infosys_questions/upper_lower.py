def upper_lower(s):
    new_str = ''
    '''#using built in function
    print(s.lower())'''

    #or using loops

    '''for i in s:
        if i.isupper():
            print(i.lower(),end="")'''

    # using ascii values to convert

    for i in s:
        if i >= 'A' and i <='Z':
            new_str = new_str + chr(ord(i) + 32)
        else:
            new_str = new_str+i

    print(new_str)


if __name__ == "__main__":
    s = input("Enter uppercase string")
    upper_lower(s)