from sys import *
import os
def DirectoryTraversal(path):
	print("Contents of the directory are")

	for Folder, Subfolder, Filename in os.walk(path):
		print("Directory name is:" +Folder)
		for sub in Subfolder:
			print("Subfolder of " +Folder+ " is " + sub)
		for file in Filename:
			print("File name is:"+file)

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