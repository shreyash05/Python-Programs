"""
1.Write a program which contains one lambda function which accepts one parameter and return
power of two.
Input : 4 Output : 16
Input : 6 Output : 64
"""
ans = lambda no : no*no 

def main():
	no = int(input("Enetr the number:"))
	ret = ans(no)
	print("answer is:",ret) 


if __name__ == '__main__':
		main()	