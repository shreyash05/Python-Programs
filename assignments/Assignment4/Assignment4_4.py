"""
4.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which are even. Map function will calculate its square.
Reduce will return addition of all that numbers.
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204
"""

import functools

FilterNnum = lambda no  : (no%2==0)
Increase = lambda no : no*no
ans  = lambda no1,no2 : no1+no2 

def main():
	arr = []
	print("Enetr the number of elements:")
	size = int(input())

	print("Eneter array elements:")
	for i in range(size):
		print("Enter element",i+1)
		no = int(input())
		arr.append(no)

	print("Array elements:",arr)
	
	ret = list(filter(FilterNnum,arr))
	print("Numbers beetween 70 and 90:",ret) 	

	ret1 = list(map(Increase,ret))
	print("Numbers after adding 10:",ret1)

	Output = functools.reduce(ans,ret1)
	print("Numbers beetween 70 and 90:",Output) 	
 	




if __name__ == '__main__':
		main()	