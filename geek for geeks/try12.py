def fix(string):
    s = set()
    list = []
    for ch in string:
        if ch not in s:
            s.add(ch)
            list.append(ch)
            print(s)
    return ''.join(list)        

string = "zvvo"
print(fix(string))


'''
remove duplicate data
zvo
'''