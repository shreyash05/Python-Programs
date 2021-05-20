from num2words import num2words
def number_to_word(no):
	return(num2words(no))

def main():
	no = int(input("Enter the number: "))
	ret = number_to_word(no)
	print(ret)

if __name__ == '__main__':
	main()	