''''
Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria : 
Unit Price First 100 units 3.5 rs  per unit
Next 100 units Rs 5 per unit 
After 200 units Rs 10 per unit 
after that 15rs per unit

1000<   meter charge= costing 10%
		tax = costing 9%

1000>   meter charge= costing 20%
		tax = costing 18%

'''

units = int(input("Enter units consumed: "))
price = 0

for i in range(1,units):
    if i<=100:
        price+=3.5
    if 100<i<=200:
        price+=5
    if 200<i<=400:
        price+=10
    if i>400:
        price+=15

meter = 0
tax = 0
if price<=1000:
    meter = price + (price*0.1)
    tax = price + (price*0.09)
else:
    meter = price + (price*0.2)
    tax = price + (price*0.18)

price = price + meter + tax


print("Your electricity bill is: ",price)