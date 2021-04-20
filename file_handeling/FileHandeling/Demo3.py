def main():
	name  = input("Enter the name of file:")
	fobj = open(name,"r")		#create new file
	size = int(input("Enter the number of elements to read"))
	print("Data from file is:")
	print(fobj.read(size))
if __name__ == '__main__':
		main()	