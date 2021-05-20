#Accept number from user and display below pattern. 
#Input : 5 
#Output : A B C D E

def display_alphabets(no):
	for i in range(no):
		print(chr(65+i), end = " ")
def main():
	print("Enter number: ")
	no = int(input())

	display_alphabets(no)

if __name__ == '__main__':
	main()	 