#3. Write a program which contains one function named as Add() which accepts two numbers
#from user and return addition of that two numbers.
#Input : 11 5 Output : 16
def Addition(no1, no2):
	return no1+no2

def main():
	print("Enetr first number:")
	no1 = int(input())

	print("Enetr second number:")
	no2 = int(input())

	ret = Addition(no1, no2)
	print("Addition is:",ret)


if __name__ == '__main__':
		main()	