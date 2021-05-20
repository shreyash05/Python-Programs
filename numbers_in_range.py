#Write a program which accept range from user and display all numbers in between
#that range.
def Display(start, end):
	if(start>end):
		print("Invalid range")
	else:	
		for i in range(start,end+1):
			print(i,end=" ")
def main():
	start = int(input("Enter start point: "))
	end = int(input("Ennter end point: "))
	Display(start, end)

if __name__ == '__main__':
		main()	