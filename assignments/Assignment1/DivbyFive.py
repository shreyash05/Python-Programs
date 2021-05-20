#7. Write a program which contains one function that accept one number from user and returns
#true if number is divisible by 5 otherwise return false.
#Input : 8 Output : False
#Input : 25 Output : True

def CheckDiv(no):
	if(no%5==0):
		return True

	else:
		return False

def main():
	print("Enter the number:")
	no = int(input())

	ret = CheckDiv(no)
	if(ret==True):
		print("True")
	else:
		print("False")	
	

if __name__ == '__main__':
		main()	