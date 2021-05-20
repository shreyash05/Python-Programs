"""
2.Write a program which contains one lambda function which accepts two parameters and return
its multiplication.
Input : 4 3 Output : 12
Input : 6 3 Output : 18
"""				

ans = lambda no1,no2 : no1*no2

def main():
	no1 = int(input("Enetr the first number:"))
	no2 = int(input("Enetr the second number:"))
	
	ret = ans(no1,no2)
	print("answer is:",ret) 


if __name__ == '__main__':
		main()	