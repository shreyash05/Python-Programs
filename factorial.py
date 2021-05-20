#Write a program to find factorial of given number.

def fcatorial(no):
	if(no<0):
		no = -no
	ifact = 1
	while(no!=0):
		ifact = ifact*no
		no = no -1

	return ifact	
def main():
	print("Enter number:")
	no = int(input())

	ret = fcatorial(no)
	print(f"Factoria of {no} is {ret}")

if __name__ == '__main__':
		main()	