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

	def EvenNum(self):
		print("Even numbers are:")
		for i in range(self.size):
			if(self.arr[i] % 2 == 0):
				print(self.arr[i],end = " ")		

	def OddNum(self):
		print("Odd numbers are:")
		for i in range(self.size):
			if(self.arr[i] % 2 != 0):
				print(self.arr[i],end = " ")

	def PrimeNum(self):
		Flag= False
		print("Prime numbers are:")
		for i in range(self.size):
			for j in range(2,int(self.arr[i]/2) + 1 ):

				if(self.arr[i] % j == 0):
					Flag=True
					break
		
			if(Flag==False):
				print(self.arr[i])	

			Flag = False		

	def PerfectNum(self):
		print("Perfect numbers are:")
		sum = 0
		for i in range(self.size):
			for j in range(1,self.arr[i]):
				if(self.arr[i] % j == 0):
					sum = sum + j

			if(sum == self.arr[i]):
				print(self.arr[i])
			sum = 0					

	def DisplayFact(self):
		for i in range(self.size):
			print("Factors of",self.arr[i])
			for j in range(1,self.arr[i]+1):
				if(self.arr[i] % j == 0):
					print(j)

	def DisplayEvenFact(self):
		for i in range(self.size):
			print("Factors of",self.arr[i])
			for j in range(1,self.arr[i]+1):
				if(self.arr[i] % j == 0):
					if(j % 2 == 0):
						print(j,end = " ")

	def SumFact(self):
		sum = 0
		for i in range(self.size):
			print("Factors of",self.arr[i])
			for j in range(1,self.arr[i]+1):
				if(self.arr[i] % j != 0):
					sum = sum + j					
		return sum

def main():
	
	print("Enter the number of elements:")
	no = int(input())
	obj = Number(no)
	
	obj.Accept()
	obj.Display()
	obj.EvenNum()
	print(" ")
	obj.OddNum()
	print(" ")
	obj.PrimeNum()
	print(" ")
	obj.PerfectNum()
	print(" ")
	obj.DisplayFact()
	print(" ")
	obj.DisplayEvenFact()
	ret1 = obj.SumFact()
	print("Summation of factores is:",ret1)

		



if __name__ == '__main__':
		main()	


