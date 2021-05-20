#Write a program which accept number from user and display its table.
def number_table(no):
	for i in range(1,11):
		print(no*i)

def main():
	no = int(input("Enter the number: "))
	number_table(no)

if __name__ == '__main__':
		main()	