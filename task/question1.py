# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

salary = int(input("Enter your salary: "))
if salary<0:
    raise Exception("Enter valid salary!")
years = int(input("Enter your year of experience: "))
if years<0:
    raise Exception("Enter valid years")

print("Your net bonus amount is: ", salary*0.05)