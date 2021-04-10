def main():
	name  = input("Enter the name of file:")
	fobj = open(name,"w")		#create new file

	str = input("Enter the data that you want to write in the file")
	fobj.write(str)		

if __name__ == '__main__':
		main()	