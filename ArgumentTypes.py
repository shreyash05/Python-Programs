#positional arguments
def Student(name,rno,address,marks):
	print("Name is:",name)
	print("Roll number is:",rno)
	print("AdDress is:",address)
	print("MArks is:",marks)

#keyword Arguments
def Computer(RAM,Processor,HDD):
	print("RAM size is:",RAM)
	print("Processor size is:",Processor)
	print("size of HDD is:",HDD)

#Default Argumnet
def CircleArea(Radius,PI=3.14):
	print("VAlue of PI is:",PI)
	return PI*Radius*Radius

def main():
	Student("Shreyash",11,"Pune",95)

	Computer(Processor="i7",RAM=8,HDD="1TB")
	Computer(RAM=16,HDD="512GB",Processor="i9")

	CircleArea(10.25)
	area1=CircleArea(10.25)
	print("area of circle is:",area1)

	CircleArea(10.25,7.12)
	area2=CircleArea(10.25,7.12)
	print("area of circle is:",area2)

if __name__ == '__main__':
			main()		