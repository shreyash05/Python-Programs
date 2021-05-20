#1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
#for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
#parameters as number and perform the operation. Write on python program which call all the
#functions from Arithmetic module by accepting the parameters from user.

from Arithmatic import*

def main():

	print("Enter first number:")
	no1 = int(input())

	print("Enter secong number:")
	no2 = int(input())

	ret = Add(no1, no2)
	print("Addition is:",ret)


	ret1 = Sub(no1, no2)
	print("Substraction is:",ret1)


	ret2 = Mul(no1, no2)
	print("Multiplication is:",ret2)


	ret3 = Div(no1, no2)
	print("Division is:",ret3)
	


if __name__ == '__main__':
		main()	