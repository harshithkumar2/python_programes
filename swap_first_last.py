lst = [1,5,3,8,9,4]

first = lst[0]
last = lst[len(lst)-1]

lst[0] , lst[len(lst)-1] = last , first

print(lst)