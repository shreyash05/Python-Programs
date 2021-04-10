#Accept n numbers from user and filter out only even numbers from that n  numbers
#after that add 2 in every even number after the addition pof 2 perform summation
#of that modified numbers.

# input [1,3,2,4,6,5,4]
#after map [2,4,6,4]
# after reduce 24

import functools
def main():
	arr = []

	print("enter the number of elements:")
	size = int(input())

	for i in range(size):
		print("Enter element number:",i+1)
		no = int(input())
		arr.append(no)

	print("Your entered data is",arr)
	#newdata = filter(Function_name,Data_list)
	newdata = list(filter(lambda no:(no%2==0),arr))		#newdata = MarvellousFilter(arr)
	print("After filtering data is:",newdata)

	newdata1 = list(map(lambda no: no+2,newdata)) 	#newdata1 = MarvellousMAp(newdata)
	print("After Mapping data is:",newdata1)

	newdata2 = functools.reduce(lambda no1,no2: no1+no2,newdata1) 		#newdata2 = MarvellousReduce(newdata1)
	print("After reduce data is:",newdata2)



if __name__ == '__main__':
		main()	