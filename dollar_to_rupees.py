def daller_to_rupees(usd):
	amount = 0
	amount = usd * 78

	return amount
	
def main():
	usd = int(input("Enter amount in daller: "))
	ret = daller_to_rupees(usd)
	print("Amount in rupees: ",ret)

if __name__ == '__main__':
		main()	