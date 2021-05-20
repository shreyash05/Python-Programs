"""
4.Write a recursive program which accept number from user and return
summation of its digits.
Input : 879
Output : 24
"""
iSum = 0
iDigit = 0

def DigitSum(no):
	global iSum
	global iDigit

	if(no != 0):
		iDigit = no % 10
		iSum = iSum+iDigit

		no = no // 10
		DigitSum(no)
	return iSum	

def main():
	no = int(input("Enter the number"))
	ret = DigitSum(no)
	print("Summation of Digits is: ",ret)


if __name__ == '__main__':
		main()	