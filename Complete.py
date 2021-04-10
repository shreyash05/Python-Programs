#Defination of Addition function
def Addition(no1, no2):
	ans = no1+no2
	return ans

#Defination of Substractiin function
def Substraction(no1, no2):
	ans = no1-no2
	return ans
#start 26 27 12 -> 19 2 19 20 7 20 22 23 27 end
#Entry point functiion
def main():
	print("Enter first number")
	value1 = int(input())

	print("Enter second number :")
	value2 = int(input())

	ret1 = Addition(value1, value2)
	ret2 = Substraction(value1, value2)

	print("Addition is :",ret1)
	print("Substraction is :",ret2)

#Code starter
if __name__ == '__main__':
		main()	