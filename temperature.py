#Write a program which accept temperature in Fahrenheit and convert it into
#celsius. (1 celsius = (Fahrenheit -32) * (5/9))
#Input : 10
#Output : -12.2222 (10 - 32) * (5/9)
#Input : 34
#Output : 1.11111 (34 - 32) * (5/9)

def fehren_to_cels(temp):
	cels = (temp -32) * (5/9)
	return cels
def main():
	print("Enter temperature in fahrenheit: ")
	temp = int(input())

	ret = fehren_to_cels(temp)
	print("Temperature in celsius:",ret)

if __name__ == '__main__':
		main()	