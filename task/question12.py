'''
Write a Python program to find the median of three values.
Expected Output:
Input first number: 15 
Input second number: 26 
Input third number: 29 
The median is 26.0
'''

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))

if n2<=n1<=n3 or n2>=n1>=n3:
    print("Median: ",n1)
elif n1<=n2<=n3 or n1>=n2>=n3:
    print("Median: ",n2)
if n1<=n3<=n2 or n1>=n3>=n2:
    print("Median: ",n3)