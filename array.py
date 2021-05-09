for i in range(3):
    for j in range(4):
        print("#",end="")
    print()
#output
####
####
####

for i in range(4):
    for j in range(4-i):
        print("#",end="")
    print()
#output
####
###
##
#

for i in range(4):
    for j in range(1+i):
        print("#",end="")
    print()
#output   
#
##
###
####