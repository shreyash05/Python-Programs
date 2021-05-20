#Write a program which accept number from user and display its digits in reverse 
#order

def digit_reverse(no):
	if (no<0):
		no = -no

	while(no!=0):
		dig = no%10
		print(dig,end = "")

		no = no//10

def main():
	print("Enter the number:")
	no = int(input())
	digit_reverse(no)
	
if __name__ == '__main__':
 	main() 