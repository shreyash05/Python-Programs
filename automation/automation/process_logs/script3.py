import psutil
from sys import *

def process_display():
	print("List of running processes")
	data=[]
	for proc in psutil.process_iter():
		value = proc.as_dict(attrs = ['pid','name','username'])
		data.append(value)

		return data
def main():
	print("Marvellous infosystems")
	print("Script Title: "+argv[0])

	"""if(len(argv) != 2):
		print("Insufficient Arguments to the script")
		exit()

	if(argv[1]=="-u") or (argv[1]=="-U"):
		print("Use the script as Name.py Parameters")
		exit()
	
	if(argv[1]=="-h") or (argv[1]=="-H"):
		print("This is a demo automation script")
		exit()"""

	arr = process_display()
	for element in arr:
		print(element)	
		
if __name__ == '__main__':
	main()	