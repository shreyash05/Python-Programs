class Base1:
	def __init__(self):
		self.i= 10
		self.j= 20
		print("Inside base constructor")

	def fun(self):
		print("inside base fun")

	def gun(self):
		print("inside base gun")


class Base2(Base):
	def __init__(self):
		Base.__init__(self)				#to call Base class contructor we have to call it from derived class cunstrutor or else gives error.
		self.x=30
		self.y=40
		print("Inside Derived cunstructor")

	def sun(self):
		print("Inside derived sun")	


	def gun(self):
		print("Inside derived gun")

class Derived(Base1,Base2):				#Multiple inheritance
	def __init__(self):
		Base1.__init__(self)
		Base2.__init__(self)
		self.a=56
		self.b=60
		print("Inside Derived2 cunstructor")


def main():


	dobj2 = Derived()				
	print(dobj.i)
	print(dobj.j)
	print(dobj.x)
	print(dobj.y)
	print(dobj.a)
	print(dobj.b)
	



if __name__ == '__main__':
		main()	