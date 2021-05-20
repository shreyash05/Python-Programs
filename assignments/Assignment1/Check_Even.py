# 2. Write a program which contains one function named as ChkNum() which accept one
#parameter as number. If number is even then it should display “Even number” otherwise
#display “Odd number” on console.
#Input : 11 Output : Odd Number
#Input : 8 Output : Even Number  

def ChkNum(no):
	if(no%2==0):
		return True
	else:
		return False

def main():

	print("Enter the number:")
	no = int(input())

	ret = ChkNum(no)
	if(ret == True):
		print("Number is even")
	else:
		print("Number is Odd")	

if __name__ == '__main__':
		main()	

