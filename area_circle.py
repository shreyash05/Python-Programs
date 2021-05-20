def circle_area(rad):
	area = 0
	area = 3.14 * rad * rad
	return area
def main():
	rad = float(input("Enter radius of circle: "))
	ret = circle_area(rad)
	print(f"Area of circle is {ret}")


if __name__ == '__main__':
		main()	