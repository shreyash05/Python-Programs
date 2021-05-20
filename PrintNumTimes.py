"""
Accept two numbers from user and display first number in second
number of times. 
"""

def DisplayNum(no1, no2):
	for i in range(no2):
		print(no1, end=" ")

def main():
	print("Enter the first number:" )
	no1 = int(input())

	print("Enter second number:")
	no2 = int(input())

	ret = DisplayNum(no1, no2)


if __name__ == '__main__':
		main()	