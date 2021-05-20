"""
3. Write a program which contains one class named as Arithmetic.
Arithmetic class contains three instance variables as Value1 ,Value2.
Inside init method initialise all instance variables to 0.
There are three instance methods inside class as Accept(), Addition(), Subtraction(),
Multiplication(), Division().
Accept method will accept value of Value1 and Value2 from user.
Addition() method will perform addition of Value1 ,Value2 and return result.
Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
Division() method will perform division of Value1 ,Value2 and return result.
After designing the above class call all instance methods by creating multiple objects.
"""
class Arithmetic:
	def __init__(self, i, j):
		self.Value1 = i
		self.Value2 = j
		

	def Accept(self):
		print("Value one is:",Value1)
		print("Value two is:",Value2)

	def Addition(self):
		return self.Value1 + self.Value2

	def Substraction(self):
		return self.Value1 - self.Value2

	def Multiplication(self):	
		return self.Value1 * self.Value2

	def Division(self):
		return self.Value1 // self.Value2	

def main():
	obj = Arithmetic(20,5)

	ret1 = obj.Addition()
	print("Addition is:",ret1)

	ret2 = obj.Substraction()
	print("Substraction is:",ret2)

	ret3 = obj.Multiplication()
	print("Multiplication is:",ret3)

	ret4 = obj.Division()
	print("Division is:",ret4)


if __name__ == '__main__':
	main()