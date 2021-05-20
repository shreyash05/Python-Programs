#Write a program which accept range from user and return addition of all even
#numbers in between that range. (Range should contains positive numbers only)

def Display(start, end):
	if(start>end):
		print("Invalid range")

	elif start<0 or end<0 :
			print("Invalid range")
	else:	
		isum = 0
		for i in range(start,end+1):
			if(i%2==0):
				isum = isum+i
		print("Addition is:",isum)
def main():
	start = int(input("Enter start point: "))
	end = int(input("Ennter end point: "))
	Display(start, end)

if __name__ == '__main__':
		main()	