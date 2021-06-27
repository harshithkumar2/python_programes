def countMin(self, Str):
        # code here
	count = 0
	high = len(Str) -1
	low = 0
	lst = list(Str)
        while not lst == lst[::-1]:
       	lst.insert(low,lst[high])
            	low +=1
            	high-=1
            	count +=1
        
        else:
       	return count
            
if __name__ = "__main__":
	string = input()
	print(countMin(string))
