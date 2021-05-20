#Write a program which accept number from user and return difference between 
#summation of even digits and summation of odd digits. 

def count_even_digit(no):
	if(no<0):
		no = -no

	esum = 0
	osum= 0	
	while(no!=0):
		idigit = no%10
		if(idigit%2==0):
			esum = esum+idigit
		elif(idigit%2!=0):
			osum = osum+idigit	
		no = no//10
	return esum-osum		

def main():
	no = int(input("Enter number: "))
	ret = count_even_digit(no)
	print("Summation is:",ret)

if __name__ == '__main__':
	main()	