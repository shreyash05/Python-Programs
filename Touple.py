def main():
	arr = (11,21,23.5,"Hello")
	print(type(arr))

	for i in range(len(arr)):
		print(arr[i])

	#arr[0] = 12		#NA	

	arr = (10,20,30,)
	print("Type of arr is",type(arr))
	
	brr = (10)		#it considered as integer without ","
	print("Type of brr is",type(brr))
	
	crr = (10,)		
	print("Type of crr is",type(crr))
if __name__ == '__main__':
		main()	