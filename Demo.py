class Number:
	

	def __init__(self,val):
		self.size = val
		self.arr = []

	def Accept(self):
		for i in range(self.size):
			print("Enter the element",i+1)
			no = int(input())
			self.arr.append(no)	

	def Display(self):
		print("Elements of list are:",self.arr)		
	
	def DisplayEvenFact(self):
		for i in range(self.size):
			print("Factors of",self.arr[i])
			for j in range(1,self.arr[i]+1):
				if(self.arr[i] % j == 0):
					if(j % 2 == 0):
						print(j)
					else:
						print("No even facors")					
	




def main():


	print("Enter the number of elements:")
	no = int(input())
	obj = Number(no)
	
	obj.Accept()
	obj.Display()
	obj.DisplayEvenFact()
	


if __name__ == '__main__':
		main()	
