"""
Write a program which accept one number from user and print that number of
even numbers on screen.
Input : 7
Output: 2 4 6 8 10 12 14 
"""

def DisplayEven(no):
	for i in range(1,no*2):
		if(i%2==0):
			print(i,end = " ")
	

def main():
	print("Enter the number:")
	no = int(input())

	DisplayEven(no)

if __name__ == '__main__':
	main()