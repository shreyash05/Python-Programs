def main():
	name  = input("Enter the name of file:")
	fobj = open(name,"r")		#create new file
	print("Single line from file is:")
	print(fobj.readline())
if __name__ == '__main__':
		main()	