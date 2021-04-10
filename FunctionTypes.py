#types of Function definations

#Accepts nothing return nothing
def fun():
	print("Inside fun")

#Accepts parameter return nothing
def gun(value):
	print("Inside gun",value)

#Accepts parameter and  return the value
def sun(value):
	value=value+1
	print("Inside sun")
	return value
#Empty function	
def mun():
	pass

def Outer():
	print("Outer function")

	def Inner():		#we cannot call inner function from outside
		print("Inner Function")
		Inner()	

def main():
	fun()
	gun(11)
	ret=sun(10)
	print(ret)
	mun()
	Outer()

if __name__ == '__main__':
		main()	
