
def Add(no1, no2):
	return no1+no2

def Sub(no1, no2):
	return no1-no2
def main():

	print("Enter first number:")
	no1 = int(input())

	print("Enter second number:")
	no2 = int(input())

	ret = Add(no1, no2)
	print("Addition is:",ret)

	ret2 = Sub(no1, no2)
	print("Substraction is:",ret2)

if __name__ == '__main__':
		main()	