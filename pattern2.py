#Write a program which accept number from user and display below pattern.
#Input : 5
#Output : * * * * * # # # # #
def display_pattern(no):
	for i in range(no):
		print("*", end = " ")
	for i in range(no):
		print("#", end = " ")	
		

def main():
	no = int(input("Enter number: "))
	display_pattern(no)

if __name__ == '__main__':
		main()	