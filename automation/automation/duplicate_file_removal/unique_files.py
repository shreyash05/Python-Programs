from sys import *
import os
import hashlib

def CalculateChecksum(path, blocksize=1024):
	fd = open(path,'rb')
	hobj = hashlib.md5()

	buffer = fd.read(blocksize)
	while len(buffer)>0:
		hobj.update(buffer)
		buffer = fd.read(blocksize)

	fd.close()
	return hobj.hexdigest()	

def DirectoryTraversal(path):
	print("Contents of the directory are")
	#set1 = set()
	dict1 = {}
	for Folder, Subfolder, Filename in os.walk(path):
		print("Directory name is:" +Folder)
		for sub in Subfolder:
			print("Subfolder of " +Folder+ " is " + sub)
		for file in Filename:
			print("File name is:"+file)
			actualpath = os.path.join(Folder,file)
			hash = CalculateChecksum(actualpath)
			#print(hash)
			#set1.add(hash)
			dict1[file]=hash
	#print(set1)			
	print(dict1)
		
def main():
	print("Marvellous infosystems")
	print("Directory traversel script")

	if(len(argv)!=2):
		print("Error:Invalide number of arguments")
		exit()

	if(argv[1] == "-h") or (argv[1] == "-H"):
		print("It is a directory cleaner script")
		exit()
	
	if(argv[1] == "-u") or (argv[1] == "-U"):
		print("Usage :Provide the absolute path of directory")
		exit()
        
	DirectoryTraversal(argv[1])

if __name__ == '__main__':
	main()	