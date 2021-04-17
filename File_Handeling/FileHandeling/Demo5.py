def main():
	name  = input("Enter the name of file:")
	fobj = open(name,"r")		#create new file
	print("Data from file is:")
	for Data in fobj:
		print(Data)
if __name__ == '__main__':
		main()	