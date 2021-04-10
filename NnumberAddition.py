def Addition(LIST):
	sum = 0
	for icnt in range(len(LIST)):
		sum = sum+LIST[icnt]
	return sum

def main():
	arr = []
	print("Enter number of elements:")
	no = int(input())

	for i in range(no):
		print("Enter element no:",i+1)
		value=int(input())
		arr.append(value)

	print("Accepted data is:",arr)	
	ret = Addition(arr)
	print("Addition of all elements is:",ret)


if __name__ == '__main__':
	main()