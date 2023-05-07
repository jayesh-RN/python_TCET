'''
A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.
'''

quantity  = int(input("Enter purchased quantity: "))
cost = quantity * 100
if cost>1000:
    print("Your total cost is: ", cost-(cost*0.1))