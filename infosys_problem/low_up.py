s=input("enter the string")
strr = ""
for i in s:
    if i >= "a" and i <= "z":
        strr =strr+ chr(ord(i)-32)
    else:
        strr=strr+i
print(strr)
    
    