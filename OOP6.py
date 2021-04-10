class Student:
	School = "Gupta"						#class variable

	def __init__(self,no1,no2,no3):
		self.m1 = no1						#instance variable
		self.m2 = no2
		self.m3 = no3

	def Instance_Totals(self):				#instance method
		print("Inside instance method")
		return self.m1+self.m2+self.m3

	@classmethod							#Decorator
	def Class_DisplaySchool(cls):			#class method
		print("School name is:",cls.School)

	@staticmethod	
	def Static_Info():
		print("This class contains information of school:")	



def main():
	Student.Class_DisplaySchool()		#calling class method
	obj1 = Student(50,80,70)			#object creation
	ret = obj1.Instance_Totals()		#calling instance method
	print("Total obtaned marks",ret)
	Student.Static_Info()				#calling static method



if __name__ == '__main__':
		main()	