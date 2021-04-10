class Arithmatic:				#class defination
	value = 101					#class variable
	def __init__(self, i, j):			#class constructor
		print("Inside constructor")
		self.no1=i 				#class instance variable
		self.no2=j				#class instance variable
	def Add(self):				#instance method	
		return self.no1+self.no2

	def Sub(self):				#instance method
		return self.no1-self.no2
	
def main():
	print("Value is:",Arithmatic.value)
	
	obj1 = Arithmatic(21,11)		#__init__(obj1,21,11)
	obj2 = Arithmatic(101,51)  		#__init__(obj2,101,51)
	print("Value is:",obj1.value)

	ret = obj1.Add()
	print("Addition is:",ret)				#ret = Add(obj1)
	ret = obj1.Sub()
	print("Substraction is:",ret)

	ret = obj2.Add()
	print("Addition is:",ret)				#ret = Add(obj1)
	ret = obj2.Sub()
	print("Substraction is:",ret)


if __name__ == '__main__':
		main()	