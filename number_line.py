#Write a program which accept number from user and print its numbers line.
#Input : 4
#Output : -4 -3 -2 -1 0 1 2 3 4 
def number_line(no):
	no1 = no
	no2 = no
	while(no1!=0):
		ino = -no1
		print(ino, end=" ")

		no1 = no1-1
	for i in range(no2+1):
		print(i, end=" ")	

def main():
	no = int(input("Enter number: "))
	number_line(no)
if __name__ == '__main__':
		main()	