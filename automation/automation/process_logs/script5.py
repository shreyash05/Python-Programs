import os
import time
import psutil
from sys import *

def process_display(folderName):
	data=[]

	if not os.path.exists(folderName):
		os.mkdir(folderName)


	else:
		print("Destination directory is already present")

	file_path = os.path.join(folderName,"Marvellous.txt")	
	fd = open(file_path,"w")

	for proc in psutil.process_iter():
		value = proc.as_dict(attrs = ['pid','name','username'])
		data.append(value)
	
	for element in data:
		fd.write("%s\n"% element)

def main():
	print("Marvellous infosystems")
	print("Script Title: "+argv[0])

	if(len(argv) != 2):
		print("Insufficient Arguments to the script")
		exit()

	if(argv[1]=="-u") or (argv[1]=="-U"):
		print("Usage: Application_Name Directory_Name")
		exit()
	
	if(argv[1]=="-h") or (argv[1]=="-H"):
		print("Help: It is used to create log filr of running processes")
		exit()

	process_display(argv[1])
		
if __name__ == '__main__':
	main()	