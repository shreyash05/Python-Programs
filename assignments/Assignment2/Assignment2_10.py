	  	
#10. Write a program which accept number from user and return addition of digits in that number.
#Input : 5187934 Output : 37

def CountDigit(iDigit):
	iSum = 0
	No = 0
	while (iDigit != 0):
 
	  	No = iDigit%10
	  	iSum=iSum+No
	  	iDigit = iDigit//10
	return iSum
	  	
def main():
	print("Enetr the number:")
	no = int(input())

	ret = CountDigit(no)
	print("Sum of digits is:",ret)

if __name__ == '__main__':
		main()	