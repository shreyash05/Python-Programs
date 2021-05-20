"""
2. Write a recursive program which display below pattern.
Input : 5
Output : 1 2 3 4 5
"""

i = 1

def Display(no):
	global i

	if(i <= no):
		print(i,end = " ")
		i = i+1
		Display(no)
		

def main():
	print("Enter the number:")
	no=int(input())

	Display(no)



if __name__ == '__main__':
		main()	


