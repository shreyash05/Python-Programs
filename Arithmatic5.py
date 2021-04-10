
def Addition(value1, value2):
	ret = value1+value2
	return ret

def main():

	no1 = int(input("Enetr first number:"))
	no2 = int(input("Eneter second number:"))

	ans = Addition(no1, no2)

	print("Addition is:",ans)

	no1 = int(input("Enetr first number:"))
	no2 = int(input("Eneter second number:"))

	ans = Addition(no1, no2)

	print("Addition is:",ans)

print(__name__)