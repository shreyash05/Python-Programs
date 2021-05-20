#1.Program to divide two numbers
def Divide(iNo1, iNo2):
	return iNo1 // iNo2

def main():
	no1 = int(input("Enetr the fist number:"))
	no2 = int(input("Enetr the second number:"))

	ret = Divide(no1, no2)
	print("Addition is:",ret)

if __name__ == '__main__':
		main()	