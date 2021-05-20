#8. Write a program which accept number from user and print that number of “*” on screen.
#Input : 5 Output : * * * * *
def PrintStar(no):
	for i in range(no):
		print("*",end=' ')

def main():
	print("Eneter the number:")
	no = int(input())

	PrintStar(no)

if __name__ == '__main__':
		main()	