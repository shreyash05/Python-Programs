class Operations:
	def __init__(self):
		pass

	def EvenNum(self,brr):
		crr = []
		for i in range(len(brr)):
			if(brr[i] % 2 == 0):
				crr.append(brr[i])

		return crr		

	def OddNum(self,brr):
		drr = []
		for i in range(len(brr)):
			if(brr[i] % 2 != 0):
				drr.append(brr[i])

		return drr		
	


def main():

	obj = Operations()

	arr = []
	print("Enter the number of elements:")
	size = int(input())
	print("Enter elements of list:")

	for i in range(size):
		
		print("Enter element",i+1)
		no = int(input())
		arr.append(no)

	ret = obj.EvenNum(arr)
	print("Even Numbers are:",ret)	

	ret1 = obj.OddNum(arr)
	print("Odd Numbers are:",ret1)	



if __name__ == '__main__':
		main()	


