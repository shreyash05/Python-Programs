"""
5.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
return Maximum number from that numbers. (You can also use normal functions instead of
lambda functions).
Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62
"""
import functools

def FilterNnum(arr):
	brr = []
	for i in range(len(arr)):
		flag = 0
		#while(j != brr[i]):
		for j in range (2,arr[i]):	
			if(arr[i]%j == 0):
				flag = 1					
				break

		if(arr[i]==1):
			pass

		else:
			if(flag == 0):
				brr.append(arr[i])
	return brr		
	
def Mult(arr):
	for i in range(len(arr)):
		arr[i] = arr[i]*2
	return arr	

def Max(arr):
	iNo = arr[0]
	for i in range(len(arr)):
		if(iNo > arr[i]):
			arr[i] = iNo

	return arr[i]		
 

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
	
	ret = FilterNnum(arr)
	#ret = list(filter(FilterNnum,arr))
	print("Prime numbers:",ret) 	

	ret1 = Mult(ret)
	print("Numbers after adding 10:",ret1)

	Output = Max(ret1)
	print("Maximum number is:",Output) 	
	




if __name__ == '__main__':
		main()	






"""
brr = []
	i =1
	#for i in range(len(arr), 2,-1):
	for i in range(1,arr[0]):
		if (arr[0] %i != 0):
			brr.append(arr[0])
	#for i in range(1, len(arr)):		
	while(i < len(arr)) :
		print(i)
		if (arr[i]==1) :
			pass
		if(arr[i] % i != 0 ):
			brr.append(arr[i])
		i = i+1	
	
	

		

	return brr		
"""
