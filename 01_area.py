import math

def main():
	r = float(input("Please enter a float number for the radius of the disc : "))
	r_area(r)

def r_area(r):
	a = math.pi * r**2
	print("Area of the disc :", a)

main()
