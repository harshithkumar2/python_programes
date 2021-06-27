inp = input("Enter data to be added to text file")

f1 = open("test.txt","a+")
f1.write(" "+inp)
f1.close()