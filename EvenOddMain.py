import EvenOddMod as EM

def main():
	print("Enter the number")
	no=int(input())
	ret = EM.EvenOdd(no)
	if(ret==True):
		print("{} Number is even".format(no))
	else:
		print("{} Number is odd".format(no))
		

if __name__ == '__main__':
	main()
