#Write a program to find odd factorial of given number.
def even_factorial(no):
	fact = 1
	if(no<0):
		no = -no
	for i in range(1,no+1):
		if(i%2!=0):
			fact = fact*i
	print(fact)			


def main():
	print("Enter number:")
	no = int(input())

	even_factorial(no)


if __name__ == '__main__':
	main()	