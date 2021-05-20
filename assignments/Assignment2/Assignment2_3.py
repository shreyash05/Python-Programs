i = 1
mul = 1
def FactorialR(val):
	global mul
	global i
	if(i <= val):
		mul = mul * i 
		i = i + 1
		FactorialR(val)

	return mul	


def Factorial(val):
	i = 1
	mul = 1

	while (i <= val):
		mul = mul*i
		i = i + 1
	return mul	
def main():
	print("Enetr the number:")
	no = int(input())

	ret = Factorial(no)
	print("Factorial of number using while loop is:",ret)

	ret1 = FactorialR(no)
	print("Factorial of number using recursion is:",ret1)

if __name__ == '__main__':
		main()	