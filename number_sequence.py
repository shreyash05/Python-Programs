#2.Write a program which accept number from user and print numbers till that
#number.
#Input : 8
#Output : 1 2 3 4 5 6 7 8
def number_sequence(no):
	for i in range(1,no+1):
		print(i)
def main():
	no = int(input("Enter number:"))
	number_sequence(no)
if __name__ == '__main__':
 	main() 