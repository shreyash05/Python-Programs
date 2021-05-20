#4. Accept one number and check whether is is divisible by 5 or not. 

def DiveFive(no):
	if( no % 5 == 0):
		return True

	else:
		return False

def main():
	print("Enetr the numbe:")
	no = int(input())

	ret = DiveFive(no)
	if(ret == True):
		print("Number is divisible by Five")

	elif (ret == False):
		print("Number is not divisibleby Five")

if __name__ == '__main__':
		main()	