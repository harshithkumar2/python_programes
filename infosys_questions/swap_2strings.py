def swap_stringd(s1,s2):
    '''s1,s2 = s2,s1

    print(s1,s2)
'''

    #   or  with 3 variable

    new_str = s1
    s1 = s2
    s2 =new_str
    print(s1,s2)



if __name__ == "__main__":
    s1 = input("Enter string1")
    s2 = input("Enter string 2")
    swap_stringd(s1,s2)