#1:Funtion accepts nothing and retun nothing
def fun():
	print("Function fun")

#2:Function which accepts parameter and return nothing
def gun(no):
	print("Function gun",no)

#3:Function which accepts parameter and return value
def sun(no):
	print("Funtion sun with parameter:",no)
	return no+1	

# 4 : Function accepts nultple values and return multiple values
def AddSub(no1, no2):
	add = no1+no2
	sub = no1-no2
	return add,sub

def Marvellous():
	print("Inside MArvellous")
	def Infosystems():
		print("Inside Infosystems")
	Infosystems()
	Infosystems()

def main():
	fun()
	gun(11)
	ret = sun(10)
	print("Return value of sun is:",ret)

	ret1,ret2 = AddSub(12,10)
	print("Addition is:",ret1)
	print("Substraction is:",ret2)

	Marvellous()

if __name__ == '__main__':
			main()		