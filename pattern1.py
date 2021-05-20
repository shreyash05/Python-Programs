""" Write a program which accept number from user and print that number of $ & *
on screen.
Input : 5
Output : $ * $ * $ * $ * $ *

Input : 3
Output : $ * $ * $ *

Input : -3
Output : $ * $ * $ *  * """
def Display_pattern(no):
	for i in range(5):
		print("$", end = " ")
		print("*", end = " ")
	

def main():
	no = int(input("ENter number:"))
	Display_pattern(no)

if __name__ == '__main__':
	main()