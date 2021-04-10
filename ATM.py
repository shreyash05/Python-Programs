import os
import threading

Amount = 1000

def ATM(func):
	func()

def Deposite():
	value = int(input("Enter amount to deposite:"))
	global Amount
	Amount = Amount+value
	print("Deposite successful - Balance:",Amount)

def Withdrow():
	value = int(input("Enter the amount to withdrow"))
	global Amount
	if value>Amount:
		print("There is no sufficient balance")
	else:
		Amount = Amount-value
		print("Withdoe successful = Balance",Amount)	

def main():
	print("Insid main")
	ATM(Deposite)
	ATM(Withdrow)

if __name__ == '__main__':
		main()	