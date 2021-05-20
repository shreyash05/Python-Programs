"""
1. Write a recursive program which display below pattern.
Input : 5
Output : * * * * *
"""
i = 1
def DisplayStar(no):
	global i 
	if(i <= no):
		print(" * ",end = " ")
		i = i+1
		DisplayStar(no)	


def main():
	print("Enter the number:")
	no = int(input())

	DisplayStar(no)




if __name__ == '__main__':
	main()