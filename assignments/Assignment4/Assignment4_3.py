"""
3.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which greater than or equal to 70 and less than or equal to
90. Map function will increase each number by 10. Reduce will return product of all that
numbers.
Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000
"""
import functools

FilterNnum = lambda no  : True if (no >= 70 and no <= 90) else False   
Increase = lambda no : no+10
ans  = lambda no1,no2 : no1*no2 

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