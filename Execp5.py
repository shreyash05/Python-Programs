class AgeInvalid(Exception):
	def __init__(self,data):
		self.data = data
def main():
	try:
		age = int(input("Enput your age for PAN card"))
		if age < 18:
			raise AgeInvalid("Your age is less than 18")

	except AgeInvalid as obj:
			print(obj)

	else:
		print("Your will ger the PAN card within 7 working days")

if __name__ == '__main__':
			main()				
