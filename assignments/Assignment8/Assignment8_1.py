#1.Design python application which creates two thread named as even and odd. Even
#thread will display first 10 even numbers and odd thread will display first 10 odd
#numbers.
import os
import threading
def even(no):
	for i in range(no):
		if(i%2==0):
			print(i)
def odd(no):
	for i in range(no):
		if(i%2!=0):
			print(i)

def main():
	value = 10
	t1 = threading.Thread(target = even, args = (value,))
	t2 = threading.Thread(target = odd, args = (value,))
    
	t1.start()
	t2.start()
	t1.join()
	t2.join()

	print("Done!")

if __name__ == '__main__':
	main()	