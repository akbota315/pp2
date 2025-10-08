#1
import math

degree = float(input("Input degree: "))
radian = degree * (math.pi / 180)
print("Output radian:", round(radian, 6))

#2
import math

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = 0.5 * (base1 + base2) * height

print("Expected Output:", area)

#3
import math

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

area = (n * (s ** 2)) / (4 * math.tan(math.pi / n))

print("The area of the polygon is:", round(area))


#4
import math

l=float(input())
h=float(input())
area=l*h

print(round(area, 1))