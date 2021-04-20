

def main():
	name = input("Eneter the name of source file")
	fobj = open(name,"r")
	name1 = input("Eneter the name of destination file")
	fobj1 = open(name1,"w")
	print("copied data is:")
	for Data in fobj:
		fobj1.write(Data)

if __name__ == '__main__':
		main()	
		