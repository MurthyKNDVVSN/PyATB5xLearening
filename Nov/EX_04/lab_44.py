# Write a Python program to calculate the
# area of a circle given its radius using the formula
# ``` area=π×r^2``` ( Take pie as 3.14)


# Logic Building Formula

# || Step 1 ||
# Figure out the inputs and output
# input -> r ->  data type -> float
# pi = 3.14
# power -> pow or ** -> any
# o/p -> float - area , print area


# || Step 2 ||
# rough logic =  area = 3.14 * pow(r,2)


# || Step 3 ||
radius = float(input("Enter the radius of the circle\n"))
print(radius)
area = 3.14987654 * (radius**2)
print("The area of the circle is:",area);
print(f"The area of the circle is:,{area:.3f}");

import math
print(math.pi)
print(math.pow(radius, 2))
area = math.pi * math.pow(radius, 2)
print("Area of the circle is --> " , area)

import math
print(math.pi)
print(math.pow(4, 2))
print(math.sin(90))
print(math.cos(90))
print(math.tan(90))