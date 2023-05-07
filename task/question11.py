'''
Write a Python program to check a triangle is . 
Note :
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides.
'''

s1 = float(input("Enter length of side1: "))
s2 = float(input("Enter length of side2: "))
s3 = float(input("Enter length of side3: "))

if s1==s2==s3:
    print("Equilateral triangle")
elif s1==s2 or s1==s3 or s2==s3:
    print("Isoceles triangle")
else:
    print("Scalene triangle")
