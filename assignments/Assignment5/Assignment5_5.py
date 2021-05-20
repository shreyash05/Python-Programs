"""
5. Write a recursive program which accept number from user and return its
factorial.
Input : 5
Output : 120
"""
i = 1
Factr = 1
def DigitSum(no):
	global i
	global Factr

	if(i <= no):
		Factr = Factr * i
		i = i + 1
		DigitSum(no)
	return Factr

def main():
	no = int(input("Enter the number"))
	ret = DigitSum(no)
	print("Factorial of number is: ",ret)


if __name__ == '__main__':
		main()	