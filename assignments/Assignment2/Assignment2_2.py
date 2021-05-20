def DisplayPattern(val):

	for i in range(val):
		for j in range(val):
			print("*",end=" ")
		print("")	

def main():
	print("Enter the number:")
	no = int(input())

	DisplayPattern(no)

if __name__ == '__main__':
		main()	