def EvenOdd(no):

	if(no%2==0):
		return True
	else:
		return False
def main():
	print("Enter the number")
	no=int(input())
	ret = EvenOdd(no)
	if(ret==True):
		print("{}Number is even",.format(no))
	else:
		print("{}Number is odd",.format(no))
		

if __name__ == '__main__':
	main()