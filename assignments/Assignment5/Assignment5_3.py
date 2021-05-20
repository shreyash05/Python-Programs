"""
3.Write a recursive program which display below pattern.
Input : 5
Output : 5 4 3 2 1
"""

i = 0
def Display(no):
	global i

	if(i < no):
		print(no - i,end = " ")
		i = i+1
		Display(no)
		

def main():
	print("Enter the number:")
	no=int(input())

	Display(no)



if __name__ == '__main__':
		main()	