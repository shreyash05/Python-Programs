class Demo:
class ClassName(object):
		"""docstring for ClassName"""
		def __init__(self, arg):
			super(ClassName, self).__init__()
			self.arg = arg
				x = 10				#class variable
	y = 20				##class variable
	def __init__(self):
		print("Inside constructor")		
		self.i = 30				#instance variable
		self.j = 40				#instance variable

	def __del__(self):
		print("Inside Distructor")

	def Fun(self):				#self=1000
		print("Innside fun")


def main():

	obj1 = Demo()
	obj2 = Demo()
	obj1.Fun()			#fun(obj1)   fun(1000)
	obj2.Fun()
	del obj1			#explicitely deleting memory (garbage collector)
	del obj2

if __name__ == '__main__':
		main()	