def rectangle_area(h1,w1):
	area = 0
	area = h1 * w1
	return area
def main():
	h1 = int(input("Enter height of rectangle: "))
	w1 = int(input("Enter width of rectangle: "))
	ret = rectangle_area(h1,w1)
	print(f"Area of rectangle is {ret}")


if __name__ == '__main__':
	main()	