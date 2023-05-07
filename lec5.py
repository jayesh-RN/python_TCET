salary = int(input("Enter your salary: "))
working = int(input("Enter your working years: "))
if working >= 5:
    salary = salary+salary*0.05
print(salary)

input = int(input("Enter your number: "))
if input < 0:
    input = input*-1
print(input)

length = int(input("Enter the length of rectangle: "))
breadth = int(input("Enter the breadth of rectangle: "))
if length == breadth:
    print("It is a square")
else:
    print("Not a square")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a > b:
    print("The greatest number is: ", a)
else:
    print("The greatest number is: ", b)

quantity = int(input("Enter the quantity: "))
cost = quantity * 100
if cost > 1000:
    discount = cost * 0.1
    print("The total cost is: ", cost - discount)
else:
    print("The total cost is: ", cost)

marks = int(input("Enter your marks: "))
if marks < 25:
    print("Your grade is: F")
elif marks >= 25 and marks < 45:
    print("Your grade is: E")
elif marks >= 45 and marks < 50:
    print("Your grade is: D")
elif marks >= 50 and marks < 60:
    print("Your grade is: C")
elif marks >= 60 and marks < 80:
    print("Your grade is: B")
else:
    print("Your grade is: A")
'''6 Take input of age of 3 people by user and determine oldest and youngest among them.'''
age1 = int(input("Enter the age of first person: "))
age2 = int(input("Enter the age of second person: "))
age3 = int(input("Enter the age of third person: "))
if age1 > age2 and age1 > age3:
    print("The oldest person is: ", age1)
elif age2 > age1 and age2 > age3:
    print("The oldest person is: ", age2)
else:
    print("The oldest person is: ", age3)
if age1 < age2 and age1 < age3:
    print("The youngest person is: ", age1)
elif age2 < age1 and age2 < age3:
    print("The youngest person is: ", age2)
else:
    print("The youngest person is: ", age3)

'''7.Write a program to print absolute value of a number entered by user. E.g.-'''
input = int(input("Enter your number: "))
if input < 0:
    input = input*-1
print(input)
'''8 A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held			-		7856
Number of classes attended.		-		856			80%
And print
percentage of class attended
Is student is allowed to sit in exam or not.

'''
classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))
percentage = (classes_attended / classes_held) * 100
if percentage < 75:
    print("You are not allowed to sit in exam")
else:
    print("You are allowed to sit in exam")
'''Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria : 
Unit Price First 100 units 3.5 rs  per unit
Next 100 units Rs 5 per unit 
After 200 units Rs 10 per unit 
after that 15rs per unit


1000<   meter charge= costing 10%
		tax = costing 9%

1000>   meter charge= costing 20%
		tax = costing 18%
'''
units = int(input("Enter the number of units: "))
if units < 100:
    cost = units * 3.5
elif units >= 100 and units < 200:
    cost = (100 * 3.5) + ((units - 100) * 5)
elif units >= 200 and units < 300:
    cost = (100 * 3.5) + (100 * 5) + ((units - 200) * 10)
else:
    cost = (100 * 3.5) + (100 * 5) + (100 * 10) + ((units - 300) * 15)
if cost < 1000:
    meter_charge = cost * 0.1
    tax = cost * 0.09
else:
    meter_charge = cost * 0.2
    tax = cost * 0.18
total_cost = cost + meter_charge + tax
print("The total cost is: ", total_cost)
'''10.Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria: 
Cost price (in Rs) 			Tax 
100000 				15 % 
> 50000 and <= 100000 		10% 
<= 50000 			5% 
'''
cost = int(input("Enter the cost price of bike: "))
if cost > 100000:
    tax = cost * 0.15
elif cost > 50000 and cost <= 100000:
    tax = cost * 0.1
else:
    tax = cost * 0.05
print("The road tax is: ", tax)
# '''11. Write a program to accept the age of a person and display the type of ticket to be purchased according to the following criteria:


year = int(input("Enter the year[yyyy]: "))
Month = int(input("Enter the month[mm]: "))
date = int(input("Enter the date[dd]: "))
if date < 30 and Month != 2:
    date = date+1
    print(date, "/", Month, "/",  year)

if date == 30 and (Month == 1 or Month == 3 or Month == 5 or Month == 7 or Month == 8 or Month == 10 or Month == 12):
    date += 1
    print(date, "/", Month, "/", year)
elif date == 30 and (Month == 4 or Month == 6 or Month == 9 or Month == 11):
    date = 1
    Month += 1
    print("date", date, "/", Month, "/", year)

if date == 31:
    date = 1
    Month += 1
    print(date, "/", Month, "/", year)

if Month == 2 and date == 28 and year % 4 != 0:
    date = 1
    Month += 1
    print(date, "/", Month, "/", year)
