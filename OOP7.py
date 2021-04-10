class Base:
	def __init__(self):
		self.i= 10
		self.j= 20
		print("Inside base constructor")

	def fun(self):
		print("inside base fun")

	def gun(self):
		print("inside base gun")


class Derived1(Base):
	def __init__(self):
		Base.__init__(self)				#to call Base class contructor we have to call it from derived class cunstrutor or else gives error.
		self.x=30
		self.y=40
		print("Inside Derived cunstructor")

	def sun(self):
		print("Inside derived sun")	


	def gun(self):
		print("Inside derived gun")

class Derived2(Derived1):			#multilevel inherirance
	def __init__(self):
		Derived1.__init__(self)
		self.a=56
		self.b=60
		print("Inside Derived2 cunstructor")


def main():

	bobj= Base()
	print(bobj.i)
	print(bobj.j)
	bobj.fun()
	bobj.gun()

	dobj= Derived1()
	print(dobj.i)
	print(dobj.j)
	print(dobj.x)
	print(dobj.y)
	dobj.fun()
	dobj.gun()			#Override

	dobj2 = Derived2()				
	print(dobj2.i)
	print(dobj2.j)
	print(dobj2.x)
	print(dobj2.y)
	print(dobj2.a)
	print(dobj2.b)
	



if __name__ == '__main__':
		main()	