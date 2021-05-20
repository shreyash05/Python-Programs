#Write a program which accept number from user and return multiplication of all 
#digits. 

def digit_multiplication(no):
	imult = 1
	while(no != 0):
		idigit = no%10
		imult = imult*idigit

		no = no //10
	return imult	
def main():
	no = int(input("Enter number:"))
	ret = digit_multiplication(no)
	print("multiplication of digits:",ret)

if __name__ == '__main__':
	main()	