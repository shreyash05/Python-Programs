""" 3. Write a program which contains one class named as Numbers.
Arithmetic class contains one instance variables as Value.
Inside init method initialise that instance variables to the value which is accepted from user.
There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),
Factors().
ChkPrime() method will returns true if number is prime otherwise return false.
ChkPerfect() method will returns true if number is perfect otherwise return false.
Factors() method will display all factors of instance variable.
SumFactors() method will return addition of all factors. Use this method in any another method
as a helper method if required.
After designing the above class call all instance methods by creating multiple objects. """
class Numbers:
	def __init__(self,value):
		self.value = value

	def ChkPrime(self):
		for element in range(2,self.value):
			flag = 0
			if(self.value%element==0):
				flag = 1
				break

		if flag == 0:
			return True
		else:
			return False			
				
	def ChkPerfect(self):
		isum = 0
		for element in range(1,self.value):
			if(self.value%element==0):
				isum = isum+element
		if isum==self.value:
			return True
		else:
			return False	

	def Factors(self):
		print("Factors of number:")
		for element in range(1,self.value):
			if(self.value%element==0):
				print(element)

	def SumFactors(self):
		isum = 0
		for element in range(1,self.value):
			if(self.value%element==0):
				isum = isum+element

		return isum		

def main():
	obj = Numbers(6)
	ret1 = obj.ChkPrime()
	if(ret1==True):
		print("Number is prime")
	else:
		print("Number is not prime")	
	ret2 = obj.ChkPerfect()
	if(ret2==True):
		print("Number is perfect")
	else:
		print("Number is not perfect")

	obj.Factors()

	ret4 = obj.SumFactors()
	print("sum of factors is:",ret4)


if __name__ == '__main__':
		main()	