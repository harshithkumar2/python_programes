def lower_upper(s):
    new_str = ''
    for i in s:
        if i >='a' and i <= 'z':
            new_str = new_str + chr(ord(i)-32)
        else:
            new_str = new_str+i

    print(new_str)

    #or built in funcion

    '''print(s.upper())'''

if __name__ == "__main__":
    s = input("Enter lowercase string")
    lower_upper(s)