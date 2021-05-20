def count_frequency_two(no):
	if(no<0):
		no = -no

	icnt = 0	
	while(no!=0):
		idigit = no%10
		if(idigit<6):
			icnt = icnt+1
		no = no//10
	return icnt	
		
def main():
	no = int(input("Enter number: "))
	ret = count_frequency_two(no)
	print("count is:",ret)
	
if __name__ == '__main__':
		main()	