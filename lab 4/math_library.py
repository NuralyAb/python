#1
import math
a=int(input("Input degree: "))
print("Output radian: ", math.radians(a))

#2
a=int(input("Height: "))
b=int(input("Base, first value: "))
c=int(input("Base, second value: "))
print("expexted output:",((b+c)/2)*a)

#3
import math
n=int(input("Input number of sides: "))
a=int(input("Input the length of a side: " ))
print("The area of the polygon is:",((n*a**2)/4)*(1/math.tan(math.radians(180/n))))

#4
a=int(input("Length of base "))
b=int(input("Height of parallelogram: "))
print("Expected output",(a*b))



