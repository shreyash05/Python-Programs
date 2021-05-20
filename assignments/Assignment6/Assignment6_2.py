"""
2. Write a program which contains one class named as Circle.
Circle class contains three instance variables as Radius ,Area, Circumference.
That class contains one class variable as PI which is initialise to 3.14.
Inside init method initialise all instance variables to 0.0.
There are three instance methods inside classas Accept() , Calculate Area() ,
CalculateCircumference(), Display().
Accept method will accept value of Radius from user.
CalculateArea() method will calculate area of circle and store it into instance variable Area.
CalculateCircumference() method will calculate circumference of circle and store it into instance
variable Circumference.
And Display() method will display value of all the instance variables as Radius , Area,
Circumference.
After designing the above class call all instance methods by creating multiple objects.

"""
class Circle:
	PI = 3.14
	def __init__(self, Radius , Area, Circumference):
		self.i = Radius
		self. j = Area
		self.k = Circumference

	def Accept(self):
		print("value of radius is:",self.i)

	def CalculateArea(self):
		self.j= Circle.PI * self.i * self.i 
		print("Area is:",self.j)	

	def CalculateCircumference(self):
		self.k = 2 * Circle.PI * self.i
		print("Circumference is:",self.k)	

def main():

	obj = Circle(5, 20, 10)
	#print("Enter the value of radius:")
	#rad = int(input())

	obj.Accept()
	obj.CalculateArea()
	obj.CalculateCircumference()



if __name__ == '__main__':
		main()	