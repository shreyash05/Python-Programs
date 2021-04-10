def Addition(data):
	sum = 0
	for i in range(len(data)):
		sum = sum + data[i]
	return sum

i = 0
sum = 0
def AdditionR(data):
	global sum
	global i

	if(i < len(data)):
		sum = sum+data[i]
		i = i+1
		AdditionR(data)
	return sum	

def main():
	arr = []
	size = int(input("Eneter the size of array:"))

	for i in range(size):arr.append(int(input()))
		#no = int(input())

	print("Data is:",arr)
		
	print("Addition is :",Addition(arr))	

	Addition(arr)
	print("recursion Addition is :",AdditionR(arr))

if __name__ == '__main__':
		main()	