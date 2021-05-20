def count_even_digit(no):
	if(no<0):
		no = -no

	icnt = 0	
	while(no!=0):
		idigit = no%10
		if(idigit%2!=0):
			icnt = icnt+1
		no = no//10
	return icnt		

def main():
	no = int(input("Enter number: "))
	ret = count_even_digit(no)
	print("Number of odd digits are:",ret)

if __name__ == '__main__':
	main()	