class Demo:
	def __init__(self, x, y):
		self.i= x 
		self.j = y

	def __add__(self, other):
		#o1  = self.i+other.i
		#no2  = self.j+other.j
		#ans = Demo(no1, no2)
		#return Demo(no1, no2)
		return Demo(self.i+other.i, self.j+other.j)

def main():
	obj1 = Demo(10,20)
	obj2 = Demo(30,40)

	ret = obj1+obj2				#obj1.__add__(obj2)		#__add__(obj1, obj2)
	print(ret.i, ret.j)
if __name__ == '__main__':
	main()	