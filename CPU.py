import os
import time
import multiprocessing


def Square(no):
	return no*no
#########################################################

def ParallelProcessing():
	start = time.time()
	print("paralell Rocessing")
	arr = range(10)
	

	pobj = multiprocessing.Pool()
	ret = pobj.map(Square,arr)
	print("Result of serial processing:",ret)
	end = time.time()
	print("Time requeired for parallel execution",end-start)

####################################################################	
def SerialProcessing():
	start = time.time()
	print("Serial proceessing")
	arr = range(10)
	ret = []

	for i in arr:
		ret.append(Square(i))

	print("Result of serial processing:",ret)
	end = time.time()
	print("Time required for Serial executuion:",end-start)	
#######################################################################

def main():
	print("Inside main")
	#print("Number of CPU cores are",os.cpu_count())
	SerialProcessing()
	ParallelProcessing()
if __name__ == '__main__':
	main()	