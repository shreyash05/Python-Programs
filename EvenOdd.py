"""
 Accept number from user and check whether number is even or
odd.
"""
def EvenOdd(no):
	if(no%2 == 0):
		return True

	else:
		return False

def main():
	print("Enter the numbe:")
	no = int(input())
	ret = EvenOdd(no)
	if(ret == True):
		print("Number is even")
	else:
		print("Number is odd")	


if __name__ == '__main__':
 	main() 