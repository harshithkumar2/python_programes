
import textwrap
s=input("enter a string")
n=int(input("enter length"))
result= "\n".join(textwrap.wrap(s,n))
print(result)