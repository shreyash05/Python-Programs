def DispalyIF(no):
	for i in range(no):		#iteration for loop
		print("Hello")
 
def DisplayR(no):
	if(no!=0):
		no = no-1
		print("Hello")
		DisplayR(no)	#Recursion	

def DisplayIW(no): 	
	while(no!=0):		#iteration while loop
		print("Hello")
		no = no-1		

def main():
	print("Enter number of iterations:")
	value = int(input())

	print("Calling iterative function using for loop")
	DispalyIF(value)

	print("Calling the recursive function")
	DisplayR(value)

	print("Calling the recursive function using while loop")
	DisplayIW(value)


if __name__ == '__main__':
		main()	

