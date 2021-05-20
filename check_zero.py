def check_zero(no):
	if(no<0):
		no = -no
	while(no!=0):
		idigit = no%10
		no = no//10
		if(idigit==0):
			return 1
			break

def main():
	no = int(input("Enter number: "))
	ret = check_zero(no)
	if(ret == 1):
		print("Number contains zero")
	else:
		print("Number not contain zero")	

if __name__ == '__main__':
		main()	