from sys import *

def function(value):
	print("Inside function with parameter: "+value)
def main():
	print("Marvellous infosystems")
	print("Script Title: "+argv[0])

	if(len(argv) != 2):
		print("Insufficient Arguments to the script")
		exit()

	if(argv[1]=="-u") or (argv[1]=="-U"):
		print("Use the script as Name.py Parameters")
		exit()
	
	if(argv[1]=="-h") or (argv[1]=="-H"):
		print("This is a demo automation script")
		exit()

	function(argv[1])	
if __name__ == '__main__':
	main()	