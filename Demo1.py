def Addition(no1, no2):
	return no1+no2
	
def main():
	print("Eneter first number:")
	value1 = int(input())

	print("Eneter second number:")
	value2 = int(input())

	ret = Addition(value1, value2)

	print("Addition is",ret)


if __name__ == '__main__':
	main()