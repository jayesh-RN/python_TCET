'''
Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria: 
Cost price (in Rs) 			Tax 
100000 				15 % 
> 50000 and <= 100000 		10% 
<= 50000 			5% 
'''

cost = int(input("Enter cost price of the bike: "))
tax = 0
if cost>100000:
    tax = cost*0.15
elif 50000<cost<=100000:
    tax = cost*0.1
elif cost>=50000:
    tax = cost*0.05

print("Road tax to be paid is: ",tax)